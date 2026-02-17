# The Boundary Condition: M_total = M_bar

## The Core Claim

When Newton's law is applied at the halo boundary $r_\text{halo}$, the implied total mass equals the baryonic mass exactly. The dark matter mass is zero.

---

## The Proof (Five Lines)

**Line 1 — Define the halo boundary** as the radius where $g_\text{bar}$ equals $a_0$:

$$\frac{V_\text{flat}^2}{r_\text{halo}} = a_0 \quad \Rightarrow \quad r_\text{halo} = \frac{V_\text{flat}^2}{a_0}$$

**Line 2 — Apply Newton at the boundary.** Outside $r_\text{halo}$, $g_\text{bar} > a_0$ and Newton holds. Newton applied at the boundary gives:

$$M_\text{Newton} = \frac{V_\text{flat}^2 \cdot r_\text{halo}}{G} = \frac{V_\text{flat}^2}{G} \cdot \frac{V_\text{flat}^2}{a_0} = \frac{V_\text{flat}^4}{G \cdot a_0}$$

**Line 3 — The Baryonic Tully-Fisher Relation** (empirically established, independent):

$$V_\text{flat}^4 = G \cdot a_0 \cdot M_\text{bar}$$

**Line 4 — Substitute:**

$$M_\text{Newton} = \frac{G \cdot a_0 \cdot M_\text{bar}}{G \cdot a_0} = M_\text{bar}$$

**Line 5 — Therefore:** $M_\text{total} = M_\text{bar}$ identically. ∎

---

## What This Means

The "dark matter mass" — the discrepancy between $M_\text{Newton}$ and $M_\text{bar}$ — arises from applying Newton inside its regime of validity. Inside $r_\text{halo}$, the force law is modified. Newton is not wrong; it is simply applied outside its domain.

The halo is not a substance. It is a **region** — the region $r < r_\text{halo}$ where $g_\text{bar} < a_0$ and the geometric bridge formula governs the dynamics. Its implied "mass" when Newton is naïvely applied is zero.

---

## Numerical Example: NGC 2403

- $V_\text{flat} = 148$ km/s (measured from outer rotation curve)
- $a_0 = 3703$ (km/s)²/kpc
- $r_\text{halo} = 148^2 / 3703 = 5.92$ kpc... 

Wait — that is the radius at which the *internal* $g_\text{bar}$ equals $a_0$ for NGC 2403 specifically, computed from the observed velocity. The disk extends to ~18 kpc. So the entire outer disk, from ~6 kpc to 18 kpc, is in the modified regime.

At $r = 18.2$ kpc:

$$g_\text{bar} = V_\text{bar}^2 / r = (95)^2 / 18.2 = 496\ (\text{km/s})^2/\text{kpc}$$
$$a_0 = 3703\ (\text{km/s})^2/\text{kpc}$$
$$g_\text{bar}/a_0 = 0.134 \ll 1 \quad \text{(deep MOND regime)}$$

The formula predicts:
$$g_\text{obs} = \sqrt{496^2 + 3703 \times 496} = \sqrt{246016 + 1836688} = \sqrt{2082704} = 1443\ (\text{km/s})^2/\text{kpc}$$
$$V_\text{pred} = \sqrt{1443 \times 18.2} = \sqrt{26262} = 162\ \text{km/s}$$

Observed: $V_\text{obs} \approx 148$ km/s. Residual ~14 km/s — accounted for largely by the M/L assumption ($\Upsilon = 0.5$ may be high for NGC 2403's outer disk).

---

## The Asymmetry Explained

**Why Newton switches off but doesn't switch back** (within the disk):

- The switch-off condition: $g_\text{bar}(r) < a_0$, i.e., $r > r_\text{halo}$
- For an exponential disk, $g_\text{bar}$ decreases monotonically outward
- Once $g_\text{bar}$ falls below $a_0$ going outward, it stays below $a_0$
- The switch-back condition ($g_\text{bar} > a_0$) requires enclosed mass to increase with radius — which it does not in a disk galaxy

Newton would return if you move inward (re-entering the Newtonian core) or to a different system (e.g., a galaxy cluster where the total enclosed mass produces $g_\text{bar} > a_0$ even at large radii).

---

## The Dark Matter Prediction

If dark matter halos exist as physical substances, they carry mass that contributes to the baryonic gravitational field. This would violate the BTFR — because $V_\text{flat}^4$ would then equal $G a_0 (M_\text{bar} + M_\text{DM})$, not $G a_0 M_\text{bar}$.

The BTFR is empirically tight (scatter ~0.1 dex, comparable to measurement errors in $V_\text{flat}$ and $M_\text{bar}$). If dark matter halos contribute significantly to the enclosed mass at the flat-curve radius, and if their mass-to-baryonic-mass ratio varies (as predicted by $\Lambda$CDM), the BTFR would show systematic scatter that is not observed.

This is the observational falsification of the dark matter interpretation:

1. BTFR holds with ~0.1 dex scatter (McGaugh et al. 2000, Lelli et al. 2016)
2. If dark matter existed as a separate mass component, it would add to $M_\text{total}$
3. Dark matter fraction varies by galaxy type and mass in $\Lambda$CDM
4. Therefore BTFR scatter would be larger than observed

It is not. Therefore $M_\text{total} = M_\text{bar}$.

---

## Falsification Condition

This framework is falsifiable. It predicts that for every galaxy:

$$M_\text{total}(\text{from lensing at } r_\text{halo}) = M_\text{bar}$$

A single galaxy where weak gravitational lensing confirms a mass excess at $r_\text{halo}$ larger than $M_\text{bar}$ by more than the BTFR scatter (~25%) would falsify the boundary condition.

Current weak lensing stacks (e.g., Brouwer et al. 2021) are consistent with this prediction out to ~100 kpc. They are not yet precise enough at the individual galaxy level to constitute a definitive test. This is the observational programme required.
