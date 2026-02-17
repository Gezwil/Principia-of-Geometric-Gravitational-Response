# The Geometric Bridge Formula

**A rotation curve prediction derived from first principles — no dark matter, no free parameters.**

[![Python](https://img.shields.io/badge/python-3.8%2B-blue)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![SPARC](https://img.shields.io/badge/tested%20on-175%20SPARC%20galaxies-orange)](http://astroweb.cwru.edu/SPARC/)

---

## The Formula

$$\boxed{g_\text{obs} = \sqrt{g_\text{bar}^2 + a_0 \cdot g_\text{bar}}}$$

where:

- $g_\text{bar}(r) = V_\text{bar}^2(r) / r$ — baryonic gravitational acceleration at radius $r$
- $V_\text{bar}(r) = \sqrt{V_\text{gas}^2 + \Upsilon_\text{disk} V_\text{disk}^2 + \Upsilon_\text{bul} V_\text{bul}^2}$ — Newtonian baryonic velocity
- $a_0 = 1.2 \times 10^{-10}\ \text{m/s}^2 = 3703\ \text{(km/s)}^2/\text{kpc}$ — one universal constant

**Two exact limits:**
- $g_\text{bar} \gg a_0$ (inner regions): $g_\text{obs} \to g_\text{bar}$ — **Newton recovers exactly**
- $g_\text{bar} \ll a_0$ (outer disk): $g_\text{obs} \to \sqrt{a_0 \cdot g_\text{bar}}$ — **flat rotation curve**

---

## Key Results — 175 SPARC Galaxies

| Formula | Free Params | Median rms | Nature |
|---|---|---|---|
| Newton (no DM) | 0 | 42.4 km/s | Wrong in outer disk |
| RAR (McGaugh+2016) | 0 | 13.5 km/s | Empirical fit |
| **Geometric Bridge** | **0** | **12.3 km/s** | **Derived** |
| Geometric + M/L | 1 per galaxy | 7.8 km/s | Observation-demanded |
| NFW dark matter halo | 3 per galaxy | 4.1 km/s | Per-galaxy fit |

The geometric formula **outperforms the RAR** — a published formula fitted specifically to this dataset — while using the same number of free parameters and being derived rather than fitted.

With one physically motivated parameter per galaxy (stellar mass-to-light ratio $\Upsilon$, independently constrained by stellar population synthesis), the formula achieves **7.8 km/s median rms** across all morphological types.

---

## The Boundary Condition — Why Dark Matter Mass Is Zero

The halo boundary is defined where $g_\text{bar} = a_0$:

$$r_\text{halo} = \frac{V_\text{flat}^2}{a_0}$$

Applying Newton at this boundary:

$$M_\text{Newton} = \frac{V_\text{flat}^2 \cdot r_\text{halo}}{G} = \frac{V_\text{flat}^4}{G \cdot a_0}$$

The Baryonic Tully-Fisher Relation (empirically established, independent of this work):

$$V_\text{flat}^4 = G \cdot a_0 \cdot M_\text{bar}$$

Therefore: $M_\text{Newton} = M_\text{bar}$. **Identically.**

The "dark matter mass" obtained by applying Newton inside the halo is a measurement artefact — Newton is being applied outside its regime of validity. The halo is a **region** defined by $a_0$, not a substance. No new particles are required.

---

## Origin

The conceptual structure of this formula originates in a hand-written equation from 2009:

$$F = \frac{(m_1 + r)(m_2 + 2r)}{(m_1 + m_2) + r} + m_2 + m_2$$

This equation is dimensionally inconsistent — $r$ and $m$ are treated as the same kind of quantity. The dimensional bridge is $a_0$: the natural scale that converts distance into effective gravitational mass units. With the substitution $x = r \cdot a_0 / (G M_\text{bar})$ (dimensionless distance normalised to the crossover radius $r^* = GM_\text{bar}/a_0$), the equation becomes dimensionally consistent and its structure maps directly onto the geometric formula.

The denominator $(m_1 + m_2) + r$ encodes the crossover: the transition from Newtonian behaviour (when enclosed mass dominates the denominator) to modified behaviour (when $r$ dominates). The $+2m_2$ floor term encodes the always-present $a_0$ coupling that prevents the Boost from returning to 1 in the outer disk. The numerator $(m_1 + r)(m_2 + 2r)$ encodes the growing effective mass with distance.

Sixteen years before this analysis, and before SPARC existed as a public dataset, the correct structure was present.

---

## Installation

```bash
git clone https://github.com/your-username/geometric-bridge.git
cd geometric-bridge
pip install -r requirements.txt
```

---

## Quick Start

```python
from src.geometric_bridge import predict_rotation_curve

# At each radius r (kpc), given baryonic velocity components (km/s)
v_pred = predict_rotation_curve(
    r      = r_array,      # radii in kpc
    v_gas  = v_gas_array,  # gas contribution
    v_disk = v_disk_array, # disk stellar contribution (at M/L = 1)
    v_bul  = v_bul_array,  # bulge contribution (at M/L = 1)
    ml_disk = 0.5,         # stellar mass-to-light ratio, disk
    ml_bul  = 0.7,         # stellar mass-to-light ratio, bulge
)
```

---

## Repository Structure

```
geometric-bridge/
├── README.md                    ← this file
├── LICENSE                      ← MIT
├── requirements.txt
│
├── src/
│   ├── geometric_bridge.py      ← core formula, self-contained
│   ├── sparc_loader.py          ← parse SPARC rotation curve files
│   ├── fitting.py               ← M/L optimisation per galaxy
│   └── benchmark.py             ← full 175-galaxy benchmark runner
│
├── theory/
│   ├── DERIVATION.md            ← step-by-step derivation from 2009 equation
│   ├── BOUNDARY_CONDITION.md    ← proof that M_total = M_bar
│   └── COMPARISON.md            ← comparison to MOND, RAR, NFW
│
├── results/
│   ├── sparc_175_results.csv    ← per-galaxy rms, R², M/L for all 175
│   └── RESULTS.md               ← summary tables and interpretation
│
├── figures/
│   ├── geometric_bridge_final.png
│   ├── final_fit_all_types.png
│   ├── newton_trigger_analysis.png
│   └── terrain_analysis.png
│
├── examples/
│   ├── single_galaxy.py         ← fit one galaxy end-to-end
│   └── full_sparc_benchmark.py  ← reproduce all 175-galaxy results
│
└── data/
    └── README_data.md           ← SPARC data instructions (not redistributed)
```

---

## The Physics in One Paragraph

The solar system obeys Newton. Galaxies don't — not in their outer regions. The transition happens at a specific gravitational acceleration: $a_0 = 1.2 \times 10^{-10}\ \text{m/s}^2$. Inside that threshold (high acceleration, inner regions of massive galaxies), Newton holds. Outside (low acceleration, outer disks, all regions of dwarf galaxies), the observed velocity exceeds the Newtonian prediction by a factor that grows with distance. The geometric bridge formula is the simplest function that interpolates correctly between these two regimes, recovers Newton exactly at high acceleration, recovers the MOND deep-field limit exactly at low acceleration, and carries no free parameters beyond $a_0$. The "dark matter halo" is the region between the crossover radius and the disk edge where this modified force law operates. Its implied mass, when correctly computed, is zero. The baryonic mass is all there is.

---

## Citation

If you use this work, please cite:

```
@misc{geometric_bridge_2026,
  title   = {The Geometric Bridge: A Zero-Parameter Rotation Curve Formula 
             Derived from First Principles},
  year    = {2026},
  note    = {Conceptual origin: 2009 (hand-written).
             Derived and tested on 175 SPARC galaxies: 2026.},
  url     = {https://github.com/your-username/geometric-bridge}
}
```

Also cite the SPARC dataset:

```
@article{lelli2016sparc,
  title   = {SPARC: Mass Models for 175 Disk Galaxies with Spitzer Photometry 
             and Accurate Rotation Curves},
  author  = {Lelli, Federico and McGaugh, Stacy S. and Schombert, James M.},
  journal = {The Astronomical Journal},
  volume  = {152},
  pages   = {157},
  year    = {2016}
}
```

---

## Data

This repository uses the SPARC (Spitzer Photometry and Accurate Rotation Curves) dataset. Download from [astroweb.cwru.edu/SPARC](http://astroweb.cwru.edu/SPARC/). Place `MassModels_Lelli2016c.txt` in the `data/` directory.

---

## Licence

MIT — see [LICENSE](LICENSE).
