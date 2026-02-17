"""
single_galaxy.py
================
Fit and plot the rotation curve for one galaxy.

Usage
-----
    python examples/single_galaxy.py data/MassModels_Lelli2016c.txt NGC3198
    python examples/single_galaxy.py data/MassModels_Lelli2016c.txt DDO154 --fixed
"""

import sys
import argparse
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams.update({'figure.facecolor': '#030308', 'axes.facecolor': '#080812',
                            'text.color': 'white', 'axes.labelcolor': 'white',
                            'xtick.color': 'white', 'ytick.color': 'white'})

# Allow running from repo root
sys.path.insert(0, str(__import__('pathlib').Path(__file__).parent.parent))

from src.sparc_loader import load_sparc, get_galaxy, HUBBLE_TYPE, MORPHOLOGY_LABEL
from src.geometric_bridge import (predict_rotation_curve, g_obs_from_g_bar,
                                   halo_boundary_radius, A0)
from src.fitting import fit_ml


def plot_galaxy(df, galaxy_name, fixed_ml=False, save=None):
    sub = get_galaxy(df, galaxy_name)
    if len(sub) < 3:
        print(f"Not enough data for {galaxy_name}")
        return

    r   = sub['r'].values
    vob = sub['V_obs'].values
    ev  = sub['eV'].values
    vg  = sub['V_gas'].values
    vd  = sub['V_disk'].values
    vb  = sub['V_bul'].values
    T   = int(sub['T'].iloc[0])
    morph = MORPHOLOGY_LABEL.get(T, f'T={T}')

    if fixed_ml:
        ml_d, ml_b = 0.5, 0.5
        label_ml = 'M/L = 0.5 (fixed)'
    else:
        result = fit_ml(r, vob, ev, vg, vd, vb)
        ml_d = result['ml_disk']
        ml_b = result['ml_bul']
        label_ml = f'M/L_disk={ml_d:.2f}, M/L_bul={ml_b:.2f} (fitted)'

    vn   = np.sqrt(np.maximum(vg, 0)**2 + ml_d*vd**2 + ml_b*vb**2)
    vpred = predict_rotation_curve(r, vg, vd, vb, ml_d, ml_b)

    rms   = float(np.sqrt(np.mean((vob - vpred)**2)))
    ss_res = float(np.sum((vob-vpred)**2))
    ss_tot = float(np.sum((vob-np.mean(vob))**2))
    r2 = 1 - ss_res/ss_tot if ss_tot > 0 else float('nan')

    v_flat  = float(np.mean(vob[-3:]))
    r_halo  = float(halo_boundary_radius(v_flat))

    # Plot
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    fig.patch.set_facecolor('#030308')

    # Left: rotation curve
    ax = axes[0]
    ax.set_facecolor('#080812')
    ax.errorbar(r, vob, yerr=ev, fmt='o', color='white', ms=5,
                elinewidth=0.9, capsize=2, label='$V_{obs}$', zorder=5)
    ax.plot(r, vn,    '--', color='#556677', lw=1.8, label='Newton ($V_{bar}$)')
    ax.plot(r, vpred, '-',  color='#00ffcc', lw=2.5,
            label=f'Geometric bridge ({rms:.1f} km/s)')
    if r_halo < r[-1] * 5:
        ax.axvline(r_halo, color='#ff9922', lw=1.5, ls=':', alpha=0.8,
                   label=f'$r_{{halo}}$ = {r_halo:.0f} kpc')
    ax.set_xlabel('Radius (kpc)', fontsize=12)
    ax.set_ylabel('$V$ (km/s)', fontsize=12)
    ax.set_title(f'{galaxy_name}  ({morph})\n{label_ml}', fontsize=11, fontweight='bold')
    ax.legend(fontsize=9, facecolor='#111', labelcolor='white')
    [sp.set_color('#1a1a2a') for sp in ax.spines.values()]
    ax.text(0.97, 0.05, f'R² = {r2:.3f}', transform=ax.transAxes,
            color='#00ffcc', fontsize=10, fontweight='bold', ha='right', va='bottom')

    # Right: Boost profile
    ax2 = axes[1]
    ax2.set_facecolor('#080812')
    gb = vn**2 / np.maximum(r, 0.001)
    boost_vals = np.sqrt(g_obs_from_g_bar(gb) / np.maximum(gb, 1e-20))
    boost_obs  = vob / np.maximum(vn, 0.01)

    ax2.scatter(r, boost_obs, color='white', s=20, zorder=5, label='$V_{obs}/V_{bar}$ (observed)')
    ax2.plot(r, boost_vals,   color='#00ffcc', lw=2.5, label='Formula prediction')
    ax2.axhline(1.0, color='#556677', lw=1.5, ls='--', label='Newton (Boost=1)')
    ax2.axvline(r_halo if r_halo < r[-1]*5 else r[-1]*2,
                color='#ff9922', lw=1.5, ls=':', alpha=0.8)

    ax2.set_xlabel('Radius (kpc)', fontsize=12)
    ax2.set_ylabel('Boost = $V_{obs}$ / $V_{bar}$', fontsize=12)
    ax2.set_title('Boost Profile\n(deviation from Newton)', fontsize=11, fontweight='bold')
    ax2.legend(fontsize=9, facecolor='#111', labelcolor='white')
    [sp.set_color('#1a1a2a') for sp in ax2.spines.values()]

    plt.tight_layout()

    print(f"\n{galaxy_name} ({morph})")
    print(f"  N points:    {len(r)}")
    print(f"  {label_ml}")
    print(f"  rms:         {rms:.2f} km/s")
    print(f"  R²:          {r2:.4f}")
    print(f"  V_flat:      {v_flat:.1f} km/s")
    print(f"  r_halo:      {r_halo:.1f} kpc  (disk extends to {r[-1]:.1f} kpc)")
    print(f"  r_halo/r_max: {r_halo/r[-1]:.2f}")

    if save:
        plt.savefig(save, dpi=200, bbox_inches='tight', facecolor='#030308')
        print(f"  Saved to: {save}")
    else:
        plt.show()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Fit single SPARC galaxy')
    parser.add_argument('sparc_file', help='Path to SPARC mass model file')
    parser.add_argument('galaxy', help='Galaxy name (e.g. NGC3198)')
    parser.add_argument('--fixed', action='store_true', help='Use fixed M/L=0.5')
    parser.add_argument('--save', default=None, help='Save figure to file')
    args = parser.parse_args()

    df = load_sparc(args.sparc_file)
    plot_galaxy(df, args.galaxy, fixed_ml=args.fixed, save=args.save)
