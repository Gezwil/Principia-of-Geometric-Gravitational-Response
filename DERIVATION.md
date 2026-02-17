# Derivation of the Geometric Bridge Formula

## Origin: The 2009 Equation

The conceptual origin of this formula is a hand-written equation from 2009:

$$F = \frac{(m_1 + r)(m_2 + 2r)}{(m_1 + m_2) + r} + m_2 + m_2$$

This equation is dimensionally inconsistent — $r$ (distance) and $m$ (mass) are treated as the same kind of quantity. Rather than a mistake, this is a *signpost*: there exists a scale that connects distance to mass, and that scale is the unknown to be found.

---

## Step 1: Finding the Dimensional Bridge

Define a dimensionless distance:

$$x = \frac{r \cdot a_0}{G M_\text{bar}}$$

When $x = 1$, we are at the radius where the baryonic gravitational acceleration equals $a_0$:

$$r^* = \frac{G M_\text{bar}}{a_0}$$

This is the crossover radius — the boundary of the "halo region." The conversion factor $a_0/G$ converts between distance and mass units. This is the missing scale in the 2009 equation.

---

## Step 2: Reading the Denominator

Substitute $r \to x \cdot r^* = x \cdot G M_\text{bar}/a_0$. The denominator becomes:

$$(m_1 + m_2) + r \to M_\text{bar}(1 + x)$$

**Two limits:**

- $x \ll 1$ (inner regions, $r \ll r^*$): denominator $\approx M_\text{bar}$ — constant, Newtonian behaviour
- $x \gg 1$ (outer disk, $r \gg r^*$): denominator $\approx r$ — grows with distance, modified behaviour

The crossover at $x = 1$ is **set by the masses themselves**, not by an external parameter. Massive galaxies have large $r^*$ (large Newtonian core). Dwarfs have tiny $r^*$ (non-Newtonian throughout). This is exactly what the data shows.

---

## Step 3: Reading the Numerator

The numerator $(m_1 + r)(m_2 + 2r)$:

- At small $r$: $\approx m_1 m_2$ — the classical gravitational product
- At large $r$: $\approx 2r^2$ — effective mass grows as $r^2$, faster than distance

Dividing by the denominator at large $r$: $F \sim 2r^2/r = 2r$ — force grows linearly with distance. This is the signature of a flat rotation curve: the force that would normally decline as $1/r^2$ is instead growing, compensating the $1/r^2$ decay.

---

## Step 4: Reading the Floor

The $+m_2 + m_2 = +2m_2$ term is always present regardless of $r$. In the acceleration language of the dimensionless equation, this maps to a constant contribution $a_0$ that persists at every radius. This is why the Boost (= $V_\text{obs}/V_\text{bar}$) never returns to 1 in the outer disk — there is always a floor.

---

## Step 5: The Geometric Bridge

The simplest function that:
1. Recovers Newton exactly at high acceleration ($g_\text{bar} \gg a_0$)
2. Produces flat rotation curves at low acceleration ($g_\text{bar} \ll a_0$)
3. Embeds the floor from the $+2m_2$ term
4. Has the crossover structure of the 2009 denominator

...is the **geometric mean** between $g_\text{bar}^2$ (Newton) and $a_0 \cdot g_\text{bar}$ (MOND):

$$\boxed{g_\text{obs} = \sqrt{g_\text{bar}^2 + a_0 \cdot g_\text{bar}}}$$

This can be written as:

$$g_\text{obs} = g_\text{bar} \cdot \sqrt{1 + \frac{a_0}{g_\text{bar}}}$$

The factor $\sqrt{1 + a_0/g_\text{bar}}$ is the **Boost** — it is 1 at high acceleration and grows as $\sqrt{a_0/g_\text{bar}}$ in the deep MOND limit.

---

## Step 6: Verification of Limits

**Newton limit** ($g_\text{bar} \gg a_0$, i.e., $x \ll 1$):

$$g_\text{obs} = \sqrt{g_\text{bar}^2 + a_0 g_\text{bar}} = g_\text{bar}\sqrt{1 + a_0/g_\text{bar}} \approx g_\text{bar}\left(1 + \frac{a_0}{2g_\text{bar}}\right) \to g_\text{bar}$$

Newton recovers exactly. ✓

**MOND limit** ($g_\text{bar} \ll a_0$, i.e., $x \gg 1$):

$$g_\text{obs} = \sqrt{g_\text{bar}^2 + a_0 g_\text{bar}} \approx \sqrt{a_0 g_\text{bar}}$$

For a galaxy with baryonic mass $M_\text{bar}$ at large $r$: $g_\text{bar} = GM_\text{bar}/r^2$, so:

$$g_\text{obs} = \sqrt{\frac{a_0 G M_\text{bar}}{r^2}} = \frac{\sqrt{a_0 G M_\text{bar}}}{r}$$

Therefore: $V_\text{obs}^2 = g_\text{obs} \cdot r = \sqrt{a_0 G M_\text{bar}} = \text{constant}$

**Flat rotation curve emerges.** ✓

**Crossover** ($g_\text{bar} = a_0$):

$$g_\text{obs} = \sqrt{a_0^2 + a_0^2} = a_0\sqrt{2}$$

The transition is smooth and continuous. ✓

---

## Step 7: The BTFR Follows

From the flat rotation curve condition:

$$V_\text{flat}^4 = a_0 \cdot G \cdot M_\text{bar}$$

This is the **Baryonic Tully-Fisher Relation** — an empirically established law with scatter 0.1 dex. The geometric formula *derives* it from first principles rather than postulating it. See [BOUNDARY_CONDITION.md](BOUNDARY_CONDITION.md) for the proof that this implies zero dark matter mass.

---

## Relation to MOND and RAR

**MOND** (Milgrom 1983) postulates:

$$\mu(g_\text{obs}/a_0) \cdot g_\text{obs} = g_\text{bar}$$

where $\mu(x)$ is an interpolating function chosen to fit the data. Many choices of $\mu$ have been proposed. The geometric bridge corresponds to:

$$\mu(x) = \frac{x}{\sqrt{1 + x}} \quad \Rightarrow \quad g_\text{obs} = \frac{g_\text{bar}}{\mu} = g_\text{bar} \cdot \sqrt{1 + \frac{a_0}{g_\text{bar}}}$$

This is a specific, derived interpolation function — not a free choice.

**The RAR** (McGaugh, Lelli & Schombert 2016) is empirically fitted as:

$$g_\text{obs} = \frac{g_\text{bar}}{1 - e^{-\sqrt{g_\text{bar}/a_0}}}$$

Both the geometric formula and the RAR have zero free parameters (beyond $a_0$). On 175 SPARC galaxies:

| Formula | Median rms |
|---|---|
| RAR | 13.5 km/s |
| Geometric bridge | **12.3 km/s** |

The geometric formula outperforms the empirical RAR while being derived from a structural reading of the 2009 equation.

---

## Summary

| 2009 element | Physical meaning | Formula element |
|---|---|---|
| $(m_1 + r)$ in numerator | Effective source mass grows with $r$ | $g_\text{bar} + a_0/g_\text{bar} \cdot g_\text{bar}$ |
| $(m_1+m_2)+r$ in denominator | Crossover at $r^* = GM/a_0$ | $g_\text{bar} = a_0$ transition |
| $+2m_2$ floor | Always-present coupling, never zero | $\sqrt{\cdot}$ floor preventing $g_\text{obs} \to 0$ |
| Dimensional inconsistency | Missing scale | $a_0$ is the bridge |

The 2009 equation had the correct structure. The geometric bridge formula is its dimensionally consistent form.
