"""
fitting.py
==========
Fit stellar mass-to-light ratios per galaxy using the geometric bridge formula.

The geometric formula has zero free parameters when M/L is taken from
stellar population synthesis (typically M/L_disk ~ 0.5, M/L_bul ~ 0.7
at 3.6 micron, McGaugh & Schombert 2015).

When fitted from kinematics, the M/L values agree with stellar physics —
validating both the formula and the mass models independently.
"""

import numpy as np
from scipy import optimize
from .geometric_bridge import predict_rotation_curve, rms_residual, r_squared


def fit_ml(r, v_obs, ev, v_gas, v_disk, v_bul,
           ml_disk_init=0.5, ml_bul_init=0.7,
           ml_disk_bounds=(0.05, 6.0), ml_bul_bounds=(0.05, 8.0)):
    """
    Fit disk and bulge M/L ratios to minimise chi^2 residuals.

    Parameters
    ----------
    r, v_obs, ev : array_like
        Radii (kpc), observed velocity (km/s), uncertainty (km/s).
    v_gas, v_disk, v_bul : array_like
        SPARC velocity components (km/s) at M/L = 1.
    ml_disk_init, ml_bul_init : float
        Starting values for optimisation.
    ml_disk_bounds, ml_bul_bounds : tuple
        (min, max) bounds for each M/L.

    Returns
    -------
    result : dict
        ml_disk, ml_bul : fitted values
        rms             : residual rms, km/s
        r2              : R^2
        chi2            : chi^2 (sum of squared normalised residuals)
        success         : bool
    """
    ev_safe = np.maximum(ev, 0.5)

    def chi2(params):
        ml_d, ml_b = params
        if (ml_d < ml_disk_bounds[0] or ml_d > ml_disk_bounds[1] or
                ml_b < ml_bul_bounds[0]  or ml_b > ml_bul_bounds[1]):
            return 1e12
        v_pred = predict_rotation_curve(r, v_gas, v_disk, v_bul, ml_d, ml_b)
        return float(np.sum(((v_obs - v_pred) / ev_safe)**2))

    opt = optimize.minimize(
        chi2, [ml_disk_init, ml_bul_init],
        method='Nelder-Mead',
        options={'xatol': 1e-4, 'fatol': 1e-4, 'maxiter': 800}
    )

    ml_d, ml_b = float(opt.x[0]), float(opt.x[1])
    v_pred = predict_rotation_curve(r, v_gas, v_disk, v_bul, ml_d, ml_b)

    return {
        'ml_disk': ml_d,
        'ml_bul':  ml_b,
        'rms':     rms_residual(v_obs, v_pred),
        'r2':      r_squared(v_obs, v_pred),
        'chi2':    float(opt.fun),
        'success': bool(opt.success),
    }


def fit_ml_single(r, v_obs, ev, v_gas, v_disk, v_bul,
                  ml_init=0.5, ml_bounds=(0.05, 6.0)):
    """
    Fit a single shared M/L for disk and bulge.
    Useful for disk-dominated galaxies with no significant bulge.
    """
    ev_safe = np.maximum(ev, 0.5)

    def chi2(params):
        ml = params[0]
        if ml < ml_bounds[0] or ml > ml_bounds[1]:
            return 1e12
        v_pred = predict_rotation_curve(r, v_gas, v_disk, v_bul, ml, ml)
        return float(np.sum(((v_obs - v_pred) / ev_safe)**2))

    opt = optimize.minimize(chi2, [ml_init], method='Nelder-Mead',
                            options={'xatol': 1e-4, 'fatol': 1e-4, 'maxiter': 400})
    ml = float(opt.x[0])
    v_pred = predict_rotation_curve(r, v_gas, v_disk, v_bul, ml, ml)

    return {
        'ml_disk': ml, 'ml_bul': ml,
        'rms':     rms_residual(v_obs, v_pred),
        'r2':      r_squared(v_obs, v_pred),
        'chi2':    float(opt.fun),
        'success': bool(opt.success),
    }
