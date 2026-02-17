"""
benchmark.py
============
Reproduce the full 175-galaxy SPARC benchmark from the paper.

Runs three modes:
    1. Zero free parameters  (M/L = 0.5 fixed)
    2. Fitted M/L            (1 or 2 free params per galaxy)
    3. Comparison formulas   (Newton, RAR)

Usage
-----
    python -m src.benchmark data/MassModels_Lelli2016c.txt
    python -m src.benchmark data/MassModels_Lelli2016c.txt --output results/
"""

import argparse
import numpy as np
import pandas as pd
from pathlib import Path

from .sparc_loader import load_sparc, get_galaxy, galaxy_list
from .geometric_bridge import (predict_rotation_curve, rms_residual, r_squared,
                                A0, halo_boundary_radius)
from .fitting import fit_ml


def _f_rar(v_gas, v_disk, v_bul, r, ml=0.5):
    """McGaugh+2016 RAR for comparison."""
    v_bar = np.sqrt(np.maximum(v_gas, 0)**2 + ml*v_disk**2 + ml*v_bul**2)
    gb    = v_bar**2 / np.maximum(r, 1e-6)
    x     = np.maximum(gb / A0, 1e-12)
    g_obs = gb / (1 - np.exp(-np.sqrt(x)))
    return np.sqrt(np.maximum(g_obs * r, 0))


def run_benchmark(sparc_path, output_dir=None, verbose=True):
    """
    Run the full benchmark.

    Parameters
    ----------
    sparc_path : str or Path
    output_dir : str or Path, optional
        If given, save CSV results there.
    verbose : bool

    Returns
    -------
    results : pd.DataFrame
        Per-galaxy results including rms and R^2 for all formula variants.
    summary : dict
        Aggregate statistics.
    """
    df = load_sparc(sparc_path)
    galaxies = galaxy_list(df)

    rows = []
    for i, gname in enumerate(galaxies):
        sub = get_galaxy(df, gname)
        if len(sub) < 3:
            continue

        r   = sub['r'].values
        vob = sub['V_obs'].values
        ev  = sub['eV'].values
        vg  = sub['V_gas'].values
        vd  = sub['V_disk'].values
        vb  = sub['V_bul'].values
        T   = int(sub['T'].iloc[0])

        # 1. Fixed M/L = 0.5
        vp_fixed = predict_rotation_curve(r, vg, vd, vb, 0.5, 0.5)
        rms_fixed = rms_residual(vob, vp_fixed)
        r2_fixed  = r_squared(vob, vp_fixed)

        # 2. Fitted M/L
        fit = fit_ml(r, vob, ev, vg, vd, vb)
        vp_fit = predict_rotation_curve(r, vg, vd, vb, fit['ml_disk'], fit['ml_bul'])
        rms_fit = rms_residual(vob, vp_fit)
        r2_fit  = r_squared(vob, vp_fit)

        # 3. Newton (no DM)
        vn = np.sqrt(np.maximum(vg, 0)**2 + 0.5*vd**2 + 0.5*vb**2)
        rms_newton = rms_residual(vob, vn)

        # 4. RAR
        vr = _f_rar(vg, vd, vb, r, ml=0.5)
        rms_rar = rms_residual(vob, vr)
        r2_rar  = r_squared(vob, vr)

        # Halo boundary
        v_flat = float(np.mean(vob[-3:]))
        r_halo = float(halo_boundary_radius(v_flat))

        rows.append({
            'Galaxy':       gname,
            'T':            T,
            'N':            len(r),
            'r_max_kpc':    float(r[-1]),
            'r_halo_kpc':   r_halo,
            'v_flat_kms':   v_flat,
            'rms_newton':   rms_newton,
            'rms_geom_fixed': rms_fixed,
            'rms_geom_fit':   rms_fit,
            'rms_rar':        rms_rar,
            'r2_geom_fixed':  r2_fixed,
            'r2_geom_fit':    r2_fit,
            'r2_rar':         r2_rar,
            'ml_disk':      fit['ml_disk'],
            'ml_bul':       fit['ml_bul'],
            'chi2_fit':     fit['chi2'],
        })

        if verbose and (i + 1) % 25 == 0:
            print(f"  {i+1}/{len(galaxies)} done...")

    results = pd.DataFrame(rows)

    summary = {
        'n_galaxies':          len(results),
        'median_rms_newton':   results['rms_newton'].median(),
        'median_rms_geom_0':   results['rms_geom_fixed'].median(),
        'median_rms_geom_fit': results['rms_geom_fit'].median(),
        'median_rms_rar':      results['rms_rar'].median(),
        'n_lt5_geom_fit':      int((results['rms_geom_fit'] < 5).sum()),
        'n_lt10_geom_fit':     int((results['rms_geom_fit'] < 10).sum()),
        'n_r2_90_geom_fit':    int((results['r2_geom_fit'] > 0.9).sum()),
        'median_ml_disk':      results['ml_disk'].median(),
    }

    if verbose:
        _print_summary(summary)

    if output_dir is not None:
        out = Path(output_dir)
        out.mkdir(parents=True, exist_ok=True)
        results.to_csv(out / 'sparc_175_results.csv', index=False)
        print(f"Results saved to {out / 'sparc_175_results.csv'}")

    return results, summary


def _print_summary(s):
    print("\n" + "="*60)
    print("BENCHMARK RESULTS — 175 SPARC GALAXIES")
    print("="*60)
    print(f"{'Formula':<30} {'Median rms (km/s)':>20}")
    print(f"  {'Newton (no DM)':<28} {s['median_rms_newton']:>20.1f}")
    print(f"  {'RAR (McGaugh+2016)':<28} {s['median_rms_rar']:>20.1f}")
    print(f"  {'Geometric (M/L=0.5)':<28} {s['median_rms_geom_0']:>20.1f}")
    print(f"  {'Geometric (fitted M/L)':<28} {s['median_rms_geom_fit']:>20.1f}")
    print()
    print(f"  rms < 5  km/s:  {s['n_lt5_geom_fit']}/175")
    print(f"  rms < 10 km/s:  {s['n_lt10_geom_fit']}/175")
    print(f"  R² > 0.9:       {s['n_r2_90_geom_fit']}/175")
    print(f"  Median M/L disk: {s['median_ml_disk']:.3f}")
    print("="*60)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Geometric Bridge SPARC Benchmark")
    parser.add_argument('sparc_file', help='Path to MassModels_Lelli2016c.txt')
    parser.add_argument('--output', default='results/', help='Output directory')
    parser.add_argument('--quiet', action='store_true')
    args = parser.parse_args()

    run_benchmark(args.sparc_file, args.output, verbose=not args.quiet)
