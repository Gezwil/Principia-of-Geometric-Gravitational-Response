# Surface Density Correlation in Galactic Rotation Curves

**Empirical correlation between baryonic surface density and rotation curve morphology**

## Overview

This repository contains analysis code and data demonstrating a strong correlation between baryonic surface density (Σ) and the rotation curve shape parameter (α) in galaxies.

**Core Finding:**
```
α = 1.972 - 0.487 × log₁₀(Σ / M☉pc⁻²)
```

**Validation:**
- **30 SPARC galaxies** (Das 2023): r = 0.970, RMSE = 0.064
- **Statistical significance:** p < 10⁻¹⁸
- **Zero free parameters** per galaxy

---

## Repository Contents

### Analysis Scripts
- `correlation_analysis.py` - Main analysis of Das (2023) parameters
- `independent_validation.py` - Tests on LITTLE THINGS and GHASP samples
- `framework_comparison.py` - Comparison of formula variants

### Data Files
- `correlation_analysis_results.csv` - Complete results for 30 SPARC galaxies
- `summary_statistics.txt` - Statistical summary
- `independent_validation_summary.txt` - Independent test results

### Visualizations
- `main_correlation_plot.png` - Primary correlation visualization
- `independent_validation.png` - Independent sample tests
- `framework_comparison_complete.png` - Formula comparison

---

## Key Results

### Das (2023) Sample Analysis

**Sample:** 30 galaxies from SPARC survey  
**Method:** Machian gravity framework fits (Das et al. 2023, arXiv:2309.00057)

| Statistic | Value |
|-----------|-------|
| Pearson correlation (r) | 0.970 |
| R² (variance explained) | 94.1% |
| RMSE | 0.064 |
| Mean absolute error | 0.042 (3.4%) |
| p-value | < 10⁻¹⁸ |

**Surface density range:** 3.6 - 218.7 M☉/pc²  
**Morphology range:** α = 1.05 - 1.65

### Sample Galaxies

| Galaxy | Σ (M☉/pc²) | α (Das) | α (Formula) | Error |
|--------|------------|---------|-------------|-------|
| CamB | 18.00 | 1.35 | 1.36 | 0.010 |
| NGC 3198 | 47.97 | 1.25 | 1.15 | 0.096 |
| NGC 2841 | 218.66 | 1.10 | 0.84 | 0.260 |
| DDO 154 | 3.63 | 1.60 | 1.69 | 0.094 |

*See `correlation_analysis_results.csv` for complete dataset*

---

## Independent Validation

### LITTLE THINGS Survey (5 dwarf galaxies)
**Accuracy:** 5/5 (100%)  
**Method:** Predicted rising curves for low-Σ dwarfs

| Galaxy | Σ | α (predicted) | Observed | Match |
|--------|---|---------------|----------|-------|
| DDO 154 | 91.8 | 1.02 | Rising | ✓ |
| DDO 168 | 92.3 | 1.01 | Rising | ✓ |
| CVnIdwA | 59.6 | 1.11 | Rising | ✓ |

### GHASP Survey (3 spiral galaxies)
**Accuracy:** 3/3 (100%)  
**Method:** Different observation technique (Hα vs HI)

| Galaxy | Σ | α (predicted) | Observed | Match |
|--------|---|---------------|----------|-------|
| UGC 10143 | 233.2 | 0.82 | Falling/Flat | ✓ |
| UGC 3382 | 38.7 | 1.20 | Flat | ✓ |
| UGC 11300 | 22.7 | 1.31 | Rising/Flat | ✓ |

**Total independent validation:** 8/8 galaxies (100%)

---

## Physical Interpretation

The correlation suggests that galactic rotation curve morphology is determined by **baryonic configuration** rather than requiring per-galaxy dark matter halo fitting.

### Proposed Mechanism

The formula may represent a **constitutive relation** for gravitational response, analogous to electromagnetic permittivity:

**Electromagnetic:**
```
D = ε(ρ) E    (dielectric response)
```

**Gravitational (proposed):**
```
g_eff = [1 + χ_g(Σ)] g_N    (geometric response)
```

Where:
- `χ_g(Σ)` is geometric susceptibility
- `Σ` is baryonic surface density
- Response depends on **configuration**, not just total mass

### Rotation Curve Model

```
V²(r) = V²_bar(r) × [1 + (r/ℓ₀)^α]
```

Where:
- `V_bar(r)` = Newtonian velocity from baryons
- `ℓ₀ ≈ 0.6 R_max` (coherence length)
- `α = α(Σ)` from empirical formula

---

## Usage

### Requirements
```bash
pip install numpy scipy matplotlib pandas
```

### Run Main Analysis
```python
python correlation_analysis.py
```

**Output:**
- Correlation statistics
- Predictions for all 30 galaxies
- Visualization plots
- CSV file with complete results

### Run Independent Validation
```python
python independent_validation.py
```

**Output:**
- LITTLE THINGS predictions (5 galaxies)
- GHASP predictions (3 galaxies)
- Combined accuracy assessment

---

## Methodology

### Surface Density Calculation

```python
# Baryonic surface density
Σ = M_bar / (π R_max²)

# Where:
# M_bar = stellar mass + gas mass (from SPARC)
# R_max = characteristic radius
```

### Formula Application

```python
import numpy as np

def predict_alpha(Sigma):
    """
    Predict rotation curve exponent from surface density
    
    Parameters:
    -----------
    Sigma : float
        Baryonic surface density in M_sun/pc^2
        
    Returns:
    --------
    alpha : float
        Rotation curve morphology parameter
    """
    return 1.972 - 0.487 * np.log10(Sigma)
```

---

## Data Sources

### Primary Dataset
**Das et al. (2023)**  
*Machian Gravity: A more accurate estimation of the mass of galaxies*  
arXiv:2309.00057  
- 30 SPARC galaxies
- Fitted α parameters
- High-quality baryonic masses

### Independent Validation
**LITTLE THINGS** (Hunter et al. 2012)  
- HI observations of dwarf irregulars
- VLA high-resolution data

**GHASP** (Garrido et al. 2002, Epinat et al. 2008)  
- Fabry-Perot Hα kinematics
- Spiral galaxy sample

### SPARC Survey
**Lelli et al. (2016)**  
*SPARC: Mass Models for 175 Disk Galaxies*  
- 3.6μm stellar masses
- HI gas distributions
- High-quality rotation curves

---

## Limitations and Caveats

### Current Limitations
1. **Sample size:** 30 galaxies for primary correlation
2. **Mass estimates:** Dependent on M/L ratios and distance measurements
3. **Independent tests:** Limited to 8 galaxies with lower-quality mass estimates
4. **Physical mechanism:** Not yet derived from first principles

### Areas for Improvement
1. **Extended validation:** Test on full 149-galaxy SPARC sample
2. **High-redshift test:** Apply to galaxies at z > 0.5
3. **Cluster scales:** Test on galaxy groups and clusters
4. **Theoretical derivation:** Connect to fundamental physics

---

## Interpretation Guidelines

### What This Finding Shows
✅ Strong empirical correlation (r = 0.97)  
✅ Predictive power on independent data  
✅ Surface density determines morphology  
✅ Zero-parameter prediction possible

### What This Finding Does NOT Show
❌ Proof of modified gravity  
❌ Disproof of dark matter  
❌ Complete theory of galaxy dynamics  
❌ Explanation at fundamental level

**Status:** Empirical correlation requiring further validation and theoretical development

---

## Citation

If you use this code or data, please cite:

**Primary analysis:**
```
Percy, G. (2026). Surface Density Correlation in Galactic Rotation Curves.
GitHub repository: https://github.com/Gezwil/Principia-of-Geometric-Gravitational-Response
```

**Original data sources:**
```
Das, S., Salucci, P., & Yadav, J. K. (2023). 
Machian Gravity: A more accurate estimation of the mass of galaxies.
arXiv:2309.00057
```

---

## Contact

**Author:** Gezwil Percy  
**Email:** academicnode14@gmail.com  
**Location:** Knysna, South Africa

### Collaboration Requests

Interested in:
- Testing on additional datasets
- Theoretical interpretation
- Co-authorship on peer-reviewed publication
- Access to SPARC full sample (149 galaxies)

**Open to feedback and collaboration from the research community.**

---

## License

MIT License - See LICENSE file for details

Data from published sources remains under original licenses.

---

## Changelog

### v1.0 (February 2026)
- Initial release
- Das (2023) correlation analysis
- Independent validation (LITTLE THINGS + GHASP)
- Framework comparison
- Complete documentation

---

## Acknowledgments

- **Dr. Santanu Das** for Machian gravity framework and fitted parameters
- **SPARC team** (Lelli et al.) for high-quality galaxy data
- **LITTLE THINGS team** (Hunter et al.) for dwarf galaxy observations
- **GHASP team** (Garrido, Epinat et al.) for Fabry-Perot kinematics

---

## Future Work

### Immediate Next Steps
1. Test on full 149-galaxy SPARC sample
2. Investigate scatter in correlation
3. Explore systematic effects
4. Develop theoretical framework

### Long-term Goals
1. First-principles derivation
2. Connection to fundamental physics
3. Cosmological implications
4. Observational predictions

---

**Last Updated:** February 8, 2026
