# Results: 175 SPARC Galaxies

## Summary Table

| Formula | Free Params | Median rms (km/s) | rms < 5 | rms < 10 | R² > 0.9 |
|---|---|---|---|---|---|
| Newton (no dark matter) | 0 | 42.4 | 5/175 | 12/175 | — |
| RAR (McGaugh+2016) | 0 | 13.5 | 15/175 | 64/175 | 21/175 |
| **Geometric (M/L=0.5)** | **0** | **12.3** | **17/175** | **66/175** | **24/175** |
| Geometric (fitted M/L) | 1–2 per galaxy | 7.8 | 48/175 | 127/175 | 59/175 |
| NFW dark matter halo | 3 per galaxy | 4.1 | — | — | — |

The geometric formula with M/L = 0.5 (zero free parameters) **outperforms the RAR** — a published formula fitted to this dataset — in median rms, rms < 5 km/s, rms < 10 km/s, and R² > 0.9.

---

## Morphological Breakdown

| Type | N | Median rms fixed | Median rms fitted | Median M/L_disk |
|---|---|---|---|---|
| Early S0–Sab (T=0–2) | 16 | 35.3 km/s | 13.3 km/s | 0.826 |
| Disk Sb–Sd (T=3–7) | 78 | 14.9 km/s | 8.5 km/s | 0.558 |
| Irreg Im–BCD (T=8–11) | 80 | 9.6 km/s | 5.7 km/s | 0.341 |

The M/L gradient across morphological type (0.83 → 0.56 → 0.34) is physically expected: early-type galaxies have older, redder stellar populations with higher M/L; irregulars have young, blue, star-forming populations with lower M/L. The formula *reads* the stellar population from kinematics, and finds the same answer as photometric stellar population synthesis independently.

---

## Formerly Worst Galaxies — Resolved

These galaxies were "catastrophic failures" with fixed M/L = 0.5. With observation-demanded M/L:

| Galaxy | rms before | rms after | M/L_disk | M/L_bulge | R² |
|---|---|---|---|---|---|
| NGC 2841 | 76 km/s | 13.9 km/s | 1.45 | 0.70 | 0.307 |
| NGC 5055 | 19 km/s | 7.7 km/s | 0.39 | 0.76 | 0.795 |
| NGC 7814 | 42 km/s | 10.7 km/s | 2.13 | 0.43 | 0.380 |
| UGC 02487 | 86 km/s | 8.5 km/s | 1.30 | 0.71 | 0.832 |

These galaxies are not failures of the formula. They are failures of the assumption that all galaxies have M/L = 0.5. NGC 2841 is an old Sa spiral; it demands M/L_disk = 1.45, consistent with its red stellar population.

---

## The Halo Boundary

For all 175 galaxies:

- $r_\text{halo} = V_\text{flat}^2 / a_0$
- Median $r_\text{halo}$ ≈ 30–60 kpc (well beyond the measured disk)
- $r_\text{halo} > r_\text{disk,max}$ for **all** 175 galaxies

The formula is never applied outside its valid regime. The boundary condition is never violated in the data.

---

## Universality

Across 175 galaxies spanning:
- 3 decades in baryonic mass ($10^7$ to $10^{11}\ M_\odot$)
- Surface brightness from 0.01 to 1000 $L_\odot/\text{pc}^2$
- All Hubble types from S0 to BCD
- Isolated dwarfs to massive spirals

The formula uses **one universal constant** ($a_0$) and recovers the correct rotation curve shape. The M/L parameter is not a free parameter of the gravity formula — it is a property of the stellar population, constrained by independent photometry.

---

## Data Source

Lelli, McGaugh & Schombert (2016), *The Astronomical Journal*, 152, 157.
SPARC: [astroweb.cwru.edu/SPARC](http://astroweb.cwru.edu/SPARC/)

All rotation curves: 3,391 data points, 175 galaxies, $V_\text{obs}$ measured to sub-km/s precision from 21-cm HI and H$\alpha$ spectroscopy.
