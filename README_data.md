# Data

## SPARC Dataset

The SPARC (Spitzer Photometry and Accurate Rotation Curves) dataset is not redistributed here. Download it directly from the authors:

**URL:** http://astroweb.cwru.edu/SPARC/

**File needed:** `MassModels_Lelli2016c.txt`

Place it in this `data/` directory before running the benchmark or examples.

## Citation for SPARC

```
@article{lelli2016sparc,
  author  = {Lelli, Federico and McGaugh, Stacy S. and Schombert, James M.},
  title   = {{SPARC}: Mass Models for 175 Disk Galaxies with {Spitzer} 
             Photometry and Accurate Rotation Curves},
  journal = {The Astronomical Journal},
  volume  = {152},
  number  = {6},
  pages   = {157},
  year    = {2016},
  doi     = {10.3847/0004-6256/152/6/157}
}
```

## Column Description (MassModels_Lelli2016c.txt)

| Column | Symbol | Units |
|---|---|---|
| 1 | Galaxy name | — |
| 2 | Distance | Mpc |
| 3 | r | kpc |
| 4 | V_obs | km/s |
| 5 | e_Vobs | km/s |
| 6 | V_gas | km/s |
| 7 | V_disk | km/s (at M/L=1) |
| 8 | V_bul | km/s (at M/L=1) |
| 9 | SB_disk | L_sun/pc² |
| 10 | SB_bul | L_sun/pc² |

Velocities are circular velocity contributions from each component. 
V_bar² = V_gas² + M/L_disk × V_disk² + M/L_bul × V_bul²
