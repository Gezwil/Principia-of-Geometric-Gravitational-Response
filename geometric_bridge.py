"""
geometric_bridge.py
===================
The Geometric Bridge Formula for galaxy rotation curves.

    g_obs = sqrt(g_bar^2 + a0 * g_bar)

Derived from first principles. Zero free parameters.
One universal constant: a0 = 1.2e-10 m/s^2.

Conceptual origin: 2009 (hand-written equation).
Tested on 175 SPARC galaxies: 2026.

Usage
-----
    from geometric_bridge import predict_rotation_curve, g_obs_from_g_bar

    # Predict full rotation curve
    v_pred = predict_rotation_curve(r, v_gas, v_disk, v_bul, ml_disk=0.5, ml_bul=0.7)

    # Work directly with accelerations
    g_observed = g_obs_from_g_bar(g_bar_array)
"""

import numpy as np

# ── Universal constant ─────────────────────────────────────────────────────────
# MOND acceleration scale
# SI: 1.2e-10 m/s^2
# Galactic units: (km/s)^2/kpc
A0_SI    = 1.2e-10          # m/s^2
KPC_M    = 3.0857e19        # metres per kpc
A0       = A0_SI * KPC_M / 1e6   # (km/s)^2 / kpc  =  3702.8

# Default stellar mass-to-light ratios (McGaugh & Schombert 2015, 3.6 micron)
ML_DISK_DEFAULT = 0.5
ML_BUL_DEFAULT  = 0.7


# ── Core formula ───────────────────────────────────────────────────────────────

def g_obs_from_g_bar(g_bar, a0=A0):
    """
    The Geometric Bridge interpolating function.

    Parameters
    ----------
    g_bar : array_like
        Baryonic gravitational acceleration, (km/s)^2/kpc.
    a0 : float
        MOND acceleration scale. Default: 3702.8 (km/s)^2/kpc.

    Returns
    -------
    g_obs : ndarray
        Observed gravitational acceleration, (km/s)^2/kpc.

    Notes
    -----
    Exact limits:
        g_bar >> a0  ->  g_obs  = g_bar          (Newton)
        g_bar << a0  ->  g_obs  = sqrt(a0*g_bar)  (MOND flat curve)
    Crossover at g_bar = a0, r* = G*M_bar/a0.
    """
    g_bar = np.asarray(g_bar, dtype=float)
    g_bar = np.maximum(g_bar, 1e-20)
    return np.sqrt(g_bar**2 + a0 * g_bar)


def v_bar_from_components(v_gas, v_disk, v_bul, ml_disk=ML_DISK_DEFAULT, ml_bul=ML_BUL_DEFAULT):
    """
    Compute Newtonian baryonic circular velocity from mass model components.

    Parameters
    ----------
    v_gas : array_like
        Gas contribution to circular velocity, km/s.
        (Already includes gas mass; sign from direction of force.)
    v_disk : array_like
        Disk stellar contribution at M/L = 1, km/s.
    v_bul : array_like
        Bulge stellar contribution at M/L = 1, km/s.
    ml_disk : float
        Disk stellar mass-to-light ratio in 3.6 micron band.
    ml_bul : float
        Bulge stellar mass-to-light ratio in 3.6 micron band.

    Returns
    -------
    v_bar : ndarray
        Baryonic circular velocity, km/s.

    Notes
    -----
    V_bar^2 = V_gas^2 + ml_disk * V_disk^2 + ml_bul * V_bul^2
    Gas component: use signed V_gas^2 = V_gas * |V_gas| to handle
    inward-pointing forces (rare but present in some galaxies).
    SPARC convention: V already encodes geometry; squaring gives V^2_circ.
    """
    v_gas  = np.asarray(v_gas,  dtype=float)
    v_disk = np.asarray(v_disk, dtype=float)
    v_bul  = np.asarray(v_bul,  dtype=float)

    v2 = (np.sign(v_gas) * v_gas**2
          + ml_disk * v_disk**2
          + ml_bul  * v_bul**2)
    return np.sqrt(np.maximum(v2, 0.0))


def predict_rotation_curve(r, v_gas, v_disk, v_bul,
                            ml_disk=ML_DISK_DEFAULT, ml_bul=ML_BUL_DEFAULT,
                            a0=A0):
    """
    Predict galaxy rotation curve from baryonic mass model.

    Parameters
    ----------
    r : array_like
        Radii, kpc.
    v_gas, v_disk, v_bul : array_like
        Velocity components as in v_bar_from_components.
    ml_disk, ml_bul : float
        Stellar mass-to-light ratios.
    a0 : float
        MOND acceleration, (km/s)^2/kpc. Default: 3702.8.

    Returns
    -------
    v_pred : ndarray
        Predicted circular velocity at each radius, km/s.

    Examples
    --------
    >>> import numpy as np
    >>> r     = np.array([1.0, 2.0, 5.0, 10.0, 20.0])
    >>> v_gas = np.array([5.0, 8.0, 15.0, 18.0, 16.0])
    >>> v_dsk = np.array([30.0, 40.0, 45.0, 40.0, 30.0])
    >>> v_bul = np.array([0.0, 0.0,  0.0,  0.0,  0.0])
    >>> v_pred = predict_rotation_curve(r, v_gas, v_dsk, v_bul)
    >>> print(v_pred.round(1))
    """
    r      = np.asarray(r,     dtype=float)
    v_bar  = v_bar_from_components(v_gas, v_disk, v_bul, ml_disk, ml_bul)
    g_bar  = v_bar**2 / np.maximum(r, 1e-6)
    g_obs  = g_obs_from_g_bar(g_bar, a0)
    return np.sqrt(np.maximum(g_obs * r, 0.0))


# ── Boost and derived quantities ───────────────────────────────────────────────

def boost(r, v_gas, v_disk, v_bul, ml_disk=ML_DISK_DEFAULT, ml_bul=ML_BUL_DEFAULT, a0=A0):
    """
    Boost factor B(r) = V_obs / V_bar = sqrt(g_obs / g_bar).

    The Boost is the ratio by which observed velocity exceeds the
    Newtonian baryonic velocity. The formula predicts:

        B(r) = (g_obs/g_bar)^0.5 = (1 + a0/g_bar)^0.25

    It equals 1 at high acceleration (Newton) and grows without bound
    as g_bar -> 0, offset by the physical floor of the disk.

    Returns
    -------
    B : ndarray
    """
    v_b  = v_bar_from_components(v_gas, v_disk, v_bul, ml_disk, ml_bul)
    gb   = v_b**2 / np.maximum(np.asarray(r, dtype=float), 1e-6)
    gobs = g_obs_from_g_bar(gb, a0)
    return np.sqrt(np.maximum(gobs / np.maximum(gb, 1e-20), 1.0))


def halo_boundary_radius(v_flat, a0=A0):
    """
    Radius at which g_bar drops to a0 — the halo boundary.

    At r_halo, Newton resumes carrying mass M_bar (see BOUNDARY_CONDITION.md).

        r_halo = V_flat^2 / a0

    Parameters
    ----------
    v_flat : float or array_like
        Asymptotic (flat) circular velocity, km/s.
    a0 : float
        MOND acceleration, (km/s)^2/kpc.

    Returns
    -------
    r_halo : float or ndarray
        Halo boundary radius, kpc.
    """
    return np.asarray(v_flat, dtype=float)**2 / a0


def baryonic_mass_from_btfr(v_flat, a0=A0, G=4.302e-6):
    """
    Baryonic mass from the Tully-Fisher Relation.

    BTFR: V_flat^4 = G * a0 * M_bar
    -> M_bar = V_flat^4 / (G * a0)

    This is identical to M_Newton = V_flat^2 * r_halo / G,
    confirming that total mass = baryonic mass at the boundary.

    Parameters
    ----------
    v_flat : float or array_like
        Flat rotation velocity, km/s.
    a0 : float
        MOND acceleration, (km/s)^2/kpc.
    G : float
        Newton's constant in kpc (km/s)^2 M_sun^-1. Default: 4.302e-6.

    Returns
    -------
    M_bar : float or ndarray
        Baryonic mass, solar masses.
    """
    v = np.asarray(v_flat, dtype=float)
    return v**4 / (G * a0)


# ── Convenience: rms and R^2 ───────────────────────────────────────────────────

def rms_residual(v_obs, v_pred):
    """Root-mean-square residual, km/s."""
    return float(np.sqrt(np.mean((np.asarray(v_obs) - np.asarray(v_pred))**2)))


def r_squared(v_obs, v_pred):
    """Coefficient of determination R^2."""
    v_obs = np.asarray(v_obs, dtype=float)
    v_pred = np.asarray(v_pred, dtype=float)
    ss_res = np.sum((v_obs - v_pred)**2)
    ss_tot = np.sum((v_obs - np.mean(v_obs))**2)
    return float(1 - ss_res / ss_tot) if ss_tot > 0 else np.nan


# ── Self-test ──────────────────────────────────────────────────────────────────

def _self_test():
    """Verify the two exact limits and the crossover condition."""
    a0 = A0

    # Limit 1: g_bar >> a0 -> g_obs ≈ g_bar
    g_high = np.array([1e6, 1e7, 1e8])  # >> a0 = 3703
    g_obs_high = g_obs_from_g_bar(g_high)
    ratio_high = g_obs_high / g_high
    assert np.allclose(ratio_high, 1.0, rtol=0.01), f"Newton limit failed: {ratio_high}"

    # Limit 2: g_bar << a0 -> g_obs ≈ sqrt(a0 * g_bar)
    g_low = np.array([0.01, 0.1, 1.0])  # << a0 = 3703
    g_obs_low = g_obs_from_g_bar(g_low)
    g_mond    = np.sqrt(a0 * g_low)
    ratio_low = g_obs_low / g_mond
    assert np.allclose(ratio_low, 1.0, rtol=0.05), f"MOND limit failed: {ratio_low}"

    # Crossover: g_bar = a0 -> g_obs = sqrt(a0^2 + a0^2) = a0*sqrt(2)
    g_cross = g_obs_from_g_bar(np.array([a0]))
    assert np.isclose(g_cross[0], a0 * np.sqrt(2), rtol=1e-6), f"Crossover failed: {g_cross}"

    # BTFR: M_Newton at r_halo = M_bar
    v_flat = 150.0  # km/s
    r_halo = halo_boundary_radius(v_flat)
    G = 4.302e-6
    m_newton = v_flat**2 * r_halo / G
    m_btfr   = baryonic_mass_from_btfr(v_flat)
    assert np.isclose(m_newton, m_btfr, rtol=1e-6), f"BTFR identity failed: {m_newton} vs {m_btfr}"

    print("All self-tests passed:")
    print(f"  Newton limit:   g_obs/g_bar = {ratio_high.mean():.6f}  (expect 1.0)")
    print(f"  MOND limit:     g_obs/g_mond = {ratio_low.mean():.4f}  (expect 1.0)")
    print(f"  Crossover:      g_obs/a0 = {g_cross[0]/a0:.6f}  (expect sqrt(2) = {np.sqrt(2):.6f})")
    print(f"  BTFR identity:  M_Newton = M_bar = {m_btfr:.3e} M_sun")


if __name__ == "__main__":
    _self_test()
