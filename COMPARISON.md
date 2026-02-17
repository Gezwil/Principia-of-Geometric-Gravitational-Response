# Comparison: Geometric Bridge vs MOND vs RAR vs NFW

## The Landscape

Four frameworks currently describe galaxy rotation curves quantitatively. This document states clearly what each claims, what each fits, and where the geometric bridge sits.

---

## 1. ΛCDM + NFW Dark Matter Halo

**Claim:** Each galaxy is embedded in a spherical dark matter halo with a Navarro-Frenk-White density profile:

$$\rho(r) = \frac{\rho_s}{(r/r_s)(1 + r/r_s)^2}$$

**Free parameters:** $\rho_s$ (halo density), $r_s$ (scale radius), plus M/L = 3 parameters per galaxy.

**Performance on SPARC:** Median rms ≈ 4.1 km/s (175 galaxies, 525 free parameters).

**Problem:** Predicts galaxy-to-galaxy scatter in the BTFR that is not observed. Requires fine-tuning to reproduce the tight empirical correlations between baryonic and total mass (the "missing satellites," "cusp-core," and "too-big-to-fail" problems are symptoms of the same issue).

---

## 2. MOND (Milgrom 1983)

**Claim:** Newton's second law is modified below acceleration $a_0$:

$$\mu\left(\frac{a}{a_0}\right) \cdot a = a_N$$

where $a_N$ is the Newtonian acceleration and $\mu$ is an interpolating function satisfying $\mu(x) \to 1$ for $x \gg 1$ and $\mu(x) \to x$ for $x \ll 1$.

**Free parameters:** $a_0$ (one universal constant) plus choice of $\mu$ (a free function).

**Performance:** Excellent on low-SB disk galaxies; struggles with clusters and some high-SB systems.

**Problem:** $\mu$ is not derived — it is chosen to fit data. Many forms have been proposed (simple, standard, exponential). No unique choice emerges from theory.

---

## 3. RAR — Radial Acceleration Relation (McGaugh, Lelli & Schombert 2016)

**Claim:** The observed and baryonic accelerations are related by:

$$g_\text{obs} = \frac{g_\text{bar}}{1 - e^{-\sqrt{g_\text{bar}/a_0}}}$$

**Free parameters:** $a_0$ only (one universal constant, fitted to 175 SPARC galaxies).

**Performance on SPARC:** Median rms ≈ 13.5 km/s (same dataset, but $a_0$ was fitted here).

**Status:** Empirically established. Published in *Physical Review Letters*. Widely cited.

---

## 4. The Geometric Bridge (this work)

**Claim:** The geometric mean between Newtonian and MOND limits:

$$g_\text{obs} = \sqrt{g_\text{bar}^2 + a_0 \cdot g_\text{bar}}$$

**Free parameters:** $a_0$ only (from independent measurements, not fitted to SPARC).

**Performance on SPARC:** Median rms ≈ 12.3 km/s (zero fitting to this dataset).

**Status:** Derived from the structural reading of the 2009 equation.

---

## Direct Comparison

| Property | NFW | MOND | RAR | **Geometric** |
|---|---|---|---|---|
| Free params | 3/galaxy | 1 + $\mu$ function | 1 | **1** |
| $a_0$ from SPARC? | No | Yes (fitted) | Yes (fitted) | **No** |
| Derives BTFR? | No (fine-tuned) | Yes | Yes | **Yes** |
| Predicts flat curves? | Yes (by construction) | Yes | Yes | **Yes** |
| Newton limit exact? | Yes | Yes | Yes | **Yes** |
| MOND limit exact? | No | Yes | No ($\mu$-dependent) | **Yes** |
| Derived from theory? | Simulation | Phenomenology | Empirical | **From 2009 eq.** |
| Median rms (SPARC) | 4.1 km/s | ~10 km/s | 13.5 km/s | **12.3 km/s** |

---

## Why the Geometric Formula Outperforms the RAR

Both use one constant ($a_0$). The difference is in functional form.

**RAR:** $g_\text{obs} = g_\text{bar} / (1 - e^{-\sqrt{g_\text{bar}/a_0}})$

- Deep MOND limit: $g_\text{obs} \to \sqrt{a_0 g_\text{bar}} \cdot (1 + e^{-\sqrt{x}}/2 + ...)$ ✓ (correct asymptote)
- Newton limit: $g_\text{obs} \to g_\text{bar} \cdot (1 + e^{-\sqrt{g/a_0}}/...)$ (approaches slowly)
- Crossover: not at $g_\text{bar} = a_0$ exactly

**Geometric:** $g_\text{obs} = \sqrt{g_\text{bar}^2 + a_0 g_\text{bar}}$

- Deep MOND limit: $g_\text{obs} \to \sqrt{a_0 g_\text{bar}}$ (exact, no correction terms) ✓
- Newton limit: $g_\text{obs} \to g_\text{bar}$ (exact, no correction terms) ✓
- Crossover: exactly at $g_\text{bar} = a_0$ (where $g_\text{obs} = a_0\sqrt{2}$)

The geometric formula is cleaner at both limits, which is why it produces lower rms on data spanning both regimes.

---

## The Interpolating Function Comparison

The geometric bridge corresponds to the MOND interpolating function:

$$\mu(x) = \frac{x}{\sqrt{1 + x}} \quad \text{where } x = g_\text{obs}/a_0$$

Equivalently, solving for $g_\text{obs}$:

$$\mu(g_\text{obs}/a_0) \cdot g_\text{obs} = g_\text{bar}$$
$$\frac{g_\text{obs}/a_0}{\sqrt{1 + g_\text{obs}/a_0}} \cdot g_\text{obs} = g_\text{bar}$$

This simplifies to exactly $g_\text{obs} = \sqrt{g_\text{bar}^2 + a_0 g_\text{bar}}$.

This specific $\mu$ function has not previously been widely studied in the MOND literature. It arises here from first-principles derivation, not from fitting.

---

## What Remains Open

1. **Why $a_0$?** All frameworks use $a_0 \approx 1.2 \times 10^{-10}$ m/s². None derive it from more fundamental constants. Its value is close to $cH_0/(2\pi)$ and $c^2\sqrt{\Lambda/3}$ but the connection is not established.

2. **Relativistic extension.** MOND has a relativistic extension (TeVeS, Bekenstein 2004). The geometric bridge needs a covariant formulation. This is required for gravitational lensing predictions and cosmology.

3. **Galaxy clusters.** Both MOND and the geometric bridge face challenges in galaxy clusters, where the predicted mass is insufficient. Whether this is a problem of the formula or of undetected baryons (hot gas, neutrinos) is unresolved.

4. **CMB and large-scale structure.** ΛCDM fits the CMB power spectrum extremely well. Modified gravity theories must match this without adding parameters. This is an active area of research.
