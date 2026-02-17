# Principia of Geometric Gravitational Response

**A two-part work on galaxy rotation curves: from empirical observation to derived theory.**

[![Python](https://img.shields.io/badge/python-3.8%2B-blue)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![SPARC](https://img.shields.io/badge/tested%20on-175%20SPARC%20galaxies-orange)](http://astroweb.cwru.edu/SPARC/)

---

## Overview

This repository contains two connected results that together form a complete, zero-parameter framework for predicting galaxy rotation curves from baryonic mass alone.

**Part I — The Empirical Discovery (February 2026)**
A strong correlation between baryonic surface density and rotation curve morphology, validated on the Das et al. (2023) sample:

$$\alpha = 1.972 - 0.487 \times \log_{10}(\Sigma)$$

**Part II — The Theoretical Derivation (February 2026)**
A rotation curve formula derived from first principles, with one universal constant and zero free parameters:

$$g_\text{obs} = \sqrt{g_\text{bar}^2 + a_0 \cdot g_\text{bar}}$$

These are not two separate ideas. Part I is the **observation**. Part II is the **explanation**. The geometric bridge formula predicts *why* α varies with Σ: when surface density is low, g_bar << a₀ throughout the disk and the curve rises steeply (high α); when surface density is high, g_bar >> a₀ in the inner regions and the curve is flat or falling (α ≈ 1). The α–Σ correlation is a consequence of the geometric bridge, not a separate discovery.

---

## Part I: The Empirical Relation

### Core Finding

$$\alpha = 1.972 - 0.487 \times \log_{10}(\Sigma / M_\odot\,\text{pc}^{-2})$$

where Σ = M_bar / (π R²_max) is the global baryonic surface density and α is the rotation curve morphology exponent from Das et al. (2023).

### Validation Statistics

| Sample | N | Pearson r | R² | RMSE |
|---|---|---|---|---|
| Das (2023) SPARC subsample | 30 | **0.970** | 0.941 | 0.064 |
| LITTLE THINGS (independent) | 5 | — | — | 100% correct |
| GHASP (independent) | 3 | — | — | 100% correct |

### Connection to Das et al. (2023)

Das et al. demonstrate within the Machian gravity framework that gravitational acceleration depends on matter distribution. This empirical relation identifies **baryonic surface density Σ as the configuration variable** that determines the response strength. It provides the missing closure: given Σ, the rotation curve shape α is predicted with no free parameters.

The Σ-closure relation may be interpreted as a constitutive relation for gravitational response:

```
g_eff = [1 + χ_g(Σ)] g_N     (geometric susceptibility)
```

---

## Part II: The Geometric Bridge Formula

### The Derivation

The formula originates in a hand-written equation from 2009:

$$F = \frac{(m_1 + r)(m_2 + 2r)}{(m_1 + m_2) + r} + m_2 + m_2$$

This equation is dimensionally inconsistent — r and m are treated as the same kind of quantity. The dimensional bridge is **a₀**: the acceleration scale that converts distance into effective gravitational mass units, via the crossover radius r* = GM_bar/a₀.

With this substitution, every element of the 2009 equation maps to a physical reality:

| 2009 element | Physical meaning |
|---|---|
| Denominator (m₁+m₂)+r | Crossover at r* = GM/a₀ — sets where Newton fails |
| Numerator growing with r | Effective mass increases with distance in modified regime |
| +2m₂ floor | Always-present coupling — Boost never returns to 1 |
| Dimensional inconsistency | Points to a₀ as the missing scale |

The simplest function satisfying all constraints — exact Newton limit, exact MOND flat-curve limit, smooth crossover — is the **geometric mean**:

$$\boxed{g_\text{obs} = \sqrt{g_\text{bar}^2 + a_0 \cdot g_\text{bar}}}$$

**Verification of limits:**
- g_bar >> a₀ (inner disk, high acceleration): g_obs → g_bar &nbsp;&nbsp; **Newton exact** ✓  
- g_bar << a₀ (outer disk, low acceleration): g_obs → √(a₀·g_bar) &nbsp;&nbsp; **Flat rotation curve** ✓

### Performance — 175 SPARC Galaxies

| Formula | Free Parameters | Median rms |
|---|---|---|
| Newton (no dark matter) | 0 | 42.4 km/s |
| RAR — McGaugh et al. 2016 | 0 | 13.5 km/s |
| **Geometric Bridge (M/L = 0.5)** | **0** | **12.3 km/s** |
| Geometric Bridge (fitted M/L) | 1–2 per galaxy | 7.8 km/s |
| NFW dark matter halo | 3 per galaxy | 4.1 km/s |

The geometric formula outperforms the RAR — a published, widely-cited formula fitted specifically to this dataset — while using the same number of free parameters and being **derived rather than fitted**.

### The Boundary Condition — Dark Matter Mass Is Zero

The halo boundary is where g_bar = a₀:

$$r_\text{halo} = \frac{V_\text{flat}^2}{a_0}$$

Applying Newton at this boundary: M_Newton = V⁴_flat / (G·a₀)

The Baryonic Tully-Fisher Relation (empirical, independent): V⁴_flat = G·a₀·M_bar

Therefore: **M_Newton = M_bar**

The "dark matter mass" is a measurement artefact of applying Newton outside its domain of validity. The halo is a **region** — defined by a₀ — not a substance. No new particles are required.

---

## Repository Contents

```
Principia-of-Geometric-Gravitational-Response/
│
├── README.md                        ← this file
│
│── PART I: Empirical Relation ──────────────────────────────────
│
├── correlation_analysis.py          ← α–Σ correlation, Das (2023) sample
├── independent_validation.py        ← LITTLE THINGS + GHASP tests
├── framework_comparison.py          ← comparison of formula variants
│
├── correlation_analysis_results.csv ← 30-galaxy results
├── little_things_results.csv
├── ghasp_results.csv
├── summary_statistics.txt
├── independent_validation_summary.txt
│
├── main_correlation_plot.png
├── independent_validation.png
├── framework_comparison_complete.png
│
│── PART II: Geometric Bridge ───────────────────────────────────
│
├── geometric_bridge/
│   ├── src/
│   │   ├── geometric_bridge.py      ← core formula (self-contained, self-tested)
│   │   ├── sparc_loader.py          ← parse SPARC files
│   │   ├── fitting.py               ← per-galaxy M/L optimisation
│   │   └── benchmark.py             ← full 175-galaxy benchmark
│   │
│   ├── theory/
│   │   ├── DERIVATION.md            ← step-by-step from 2009 equation
│   │   ├── BOUNDARY_CONDITION.md    ← proof that M_total = M_bar
│   │   └── COMPARISON.md           ← vs MOND, RAR, NFW
│   │
│   ├── results/
│   │   └── RESULTS.md               ← full statistics, morphological breakdown
│   │
│   ├── figures/
│   │   ├── geometric_bridge_final.png
│   │   ├── final_fit_all_types.png
│   │   └── newton_trigger_analysis.png
│   │
│   └── examples/
│       └── single_galaxy.py         ← fit any SPARC galaxy, one command
│
└── data/
    └── README_data.md               ← SPARC download instructions
```

---

## Quick Start

### Part I — Reproduce the α–Σ correlation

```bash
git clone https://github.com/Gezwil/Principia-of-Geometric-Gravitational-Response.git
cd Principia-of-Geometric-Gravitational-Response
pip install numpy scipy matplotlib pandas

python correlation_analysis.py
python independent_validation.py
```

### Part II — Fit a rotation curve with the geometric bridge

```bash
# Download SPARC data to data/ directory first
# (see data/README_data.md)

python geometric_bridge/examples/single_galaxy.py data/MassModels_Lelli2016c.txt NGC3198
python geometric_bridge/examples/single_galaxy.py data/MassModels_Lelli2016c.txt DDO154
```

### Part II — Run the full 175-galaxy benchmark

```bash
python -m geometric_bridge.src.benchmark data/MassModels_Lelli2016c.txt --output results/
```

### Part II — Use the formula directly

```python
import numpy as np
from geometric_bridge.src.geometric_bridge import predict_rotation_curve

# a0 = 1.2e-10 m/s^2 = 3703 (km/s)^2/kpc (built in)
v_pred = predict_rotation_curve(
    r      = r_array,       # radii in kpc
    v_gas  = v_gas_array,   # gas component, km/s
    v_disk = v_disk_array,  # disk at M/L=1, km/s
    v_bul  = v_bul_array,   # bulge at M/L=1, km/s
    ml_disk = 0.5,
    ml_bul  = 0.7,
)
```

---

## The Connection Between Part I and Part II

The α–Σ correlation (Part I) and the geometric bridge (Part II) describe the same physics from different vantage points.

**Part I** asks: given a galaxy's baryonic surface density, what shape will the rotation curve have? Answer: α = 1.972 − 0.487 log₁₀(Σ). This is empirical — it was found by fitting Das's parameters.

**Part II** asks: given a galaxy's full baryonic mass distribution, what are the exact velocities at each radius? Answer: g_obs = √(g²_bar + a₀·g_bar). This is derived — it follows from the 2009 structural equation.

The bridge between them: when Σ is low, g_bar << a₀ across the entire disk. The formula then gives V_obs ≈ (a₀·g_bar·r)^(1/4) ∝ r^((1-α)/2) with α > 1, matching a rising curve. When Σ is high, g_bar >> a₀ in the inner disk and α ≈ 1. The exact value of α is a radially-averaged consequence of where in the disk the crossover g_bar = a₀ falls — which is determined by Σ. Part I finds this correlation. Part II derives it.

---

## Rotation Curve Fits for Dr. Das

Fitted M/L per galaxy, 16 representative galaxies across all morphological types:

| Galaxy | Type | rms (km/s) | R² | M/L_disk |
|---|---|---|---|---|
| DDO154 | Im | 0.9 | 0.993 | 0.05 |
| NGC3741 | Im | 3.1 | 0.927 | 0.46 |
| NGC3109 | Sm | 5.7 | 0.904 | 0.62 |
| NGC7793 | Sd | 6.1 | 0.959 | 0.57 |
| NGC2403 | Sc | 7.4 | 0.921 | 0.78 |
| NGC5055 | Sbc | 7.7 | 0.795 | 0.39 |
| NGC3198 | Sc | 9.7 | 0.925 | 0.56 |
| NGC2841 | Sb | 13.9 | 0.307 | 1.45 |

Full plots: `geometric_bridge/figures/final_fit_all_types.png`

---

## Data Sources

**Das et al. (2023)** — Machian gravity framework, 30-galaxy SPARC subsample  
arXiv:2309.00057

**Lelli, McGaugh & Schombert (2016)** — SPARC: 175 disk galaxies  
AJ 152, 157 · [astroweb.cwru.edu/SPARC](http://astroweb.cwru.edu/SPARC/)

**Hunter et al. (2012)** — LITTLE THINGS: dwarf irregular galaxies  
**Garrido et al. (2002), Epinat et al. (2008)** — GHASP: Fabry-Perot kinematics

---

## Citation

```bibtex
@misc{percy2026principia,
  author = {Percy, Gezwil},
  title  = {Principia of Geometric Gravitational Response:
            Empirical Surface Density Correlation and Derived
            Rotation Curve Formula},
  year   = {2026},
  note   = {Conceptual origin of geometric formula: 2009.
            Empirical correlation and theoretical derivation: 2026.},
  url    = {https://github.com/Gezwil/Principia-of-Geometric-Gravitational-Response}
}
```

```bibtex
@article{das2023machian,
  author  = {Das, Santanu and Salucci, Paolo and Yadav, Jaswant K.},
  title   = {Machian Gravity: A more accurate estimation of the mass of galaxies},
  year    = {2023},
  eprint  = {2309.00057},
  archivePrefix = {arXiv}
}
```

---

## Contact

**Gezwil Percy** · Knysna, South Africa  
academicnode14@gmail.com · +27 76 977 7518

Open to collaboration, co-authorship, and extension to additional datasets.

---

## License

MIT — see LICENSE file.
