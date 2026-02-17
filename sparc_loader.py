"""
sparc_loader.py
===============
Parse SPARC rotation curve mass model files.

SPARC: Spitzer Photometry and Accurate Rotation Curves
Lelli, McGaugh & Schombert 2016, AJ 152, 157
Data: http://astroweb.cwru.edu/SPARC/

File format: MassModels_Lelli2016c.txt
Columns: Galaxy, Dist, r, V_obs, e_Vobs, V_gas, V_disk, V_bul, SB_disk, SB_bul
"""

import numpy as np
import pandas as pd
from pathlib import Path


SPARC_COLUMNS = [
    'Galaxy', 'Dist', 'r', 'V_obs', 'eV', 'V_gas', 'V_disk', 'V_bul', 'SB_disk', 'SB_bul'
]

# Hubble type T for each SPARC galaxy
# T: 0=S0, 1=Sa, 2=Sab, 3=Sb, 4=Sbc, 5=Sc, 6=Scd, 7=Sd, 8=Sdm, 9=Sm, 10=Im, 11=BCD
HUBBLE_TYPE = {
    'CamB':10,'D512-2':10,'D564-8':10,'D631-7':10,'DDO064':10,'DDO154':10,
    'DDO161':10,'DDO168':10,'DDO170':10,'ESO079-G014':4,'ESO116-G012':7,
    'ESO444-G084':10,'ESO563-G021':4,'F561-1':9,'F563-1':9,'F563-V1':10,
    'F563-V2':10,'F565-V2':10,'F567-2':9,'F568-1':5,'F568-3':7,'F568-V1':7,
    'F571-8':5,'F571-V1':7,'F574-1':7,'F574-2':9,'F579-V1':5,'F583-1':9,
    'F583-4':5,'IC2574':9,'IC4202':4,'KK98-251':10,'NGC0024':5,'NGC0055':9,
    'NGC0100':6,'NGC0247':7,'NGC0289':4,'NGC0300':7,'NGC0801':5,'NGC0891':3,
    'NGC1003':6,'NGC1090':4,'NGC1705':11,'NGC2366':10,'NGC2403':6,'NGC2683':3,
    'NGC2841':3,'NGC2903':4,'NGC2915':11,'NGC2955':3,'NGC2976':5,'NGC2998':5,
    'NGC3109':9,'NGC3198':5,'NGC3521':4,'NGC3726':5,'NGC3741':10,'NGC3769':3,
    'NGC3877':5,'NGC3893':5,'NGC3917':6,'NGC3949':4,'NGC3953':4,'NGC3972':4,
    'NGC3992':4,'NGC4010':7,'NGC4013':3,'NGC4051':4,'NGC4068':10,'NGC4085':5,
    'NGC4088':4,'NGC4100':4,'NGC4138':0,'NGC4157':3,'NGC4183':6,'NGC4214':10,
    'NGC4217':3,'NGC4389':4,'NGC4559':6,'NGC5005':4,'NGC5033':5,'NGC5055':4,
    'NGC5371':4,'NGC5585':7,'NGC5907':5,'NGC5985':3,'NGC6015':6,'NGC6195':3,
    'NGC6503':6,'NGC6674':3,'NGC6789':11,'NGC6946':6,'NGC7331':3,'NGC7793':7,
    'NGC7814':2,'PGC51017':11,'UGC00128':8,'UGC00191':9,'UGC00634':9,
    'UGC00731':10,'UGC00891':9,'UGC01230':9,'UGC01281':8,'UGC02023':10,
    'UGC02259':8,'UGC02487':0,'UGC02885':5,'UGC02916':2,'UGC02953':2,
    'UGC03205':2,'UGC03546':1,'UGC03580':1,'UGC04278':7,'UGC04305':10,
    'UGC04325':9,'UGC04483':10,'UGC04499':8,'UGC05005':10,'UGC05253':2,
    'UGC05414':10,'UGC05716':9,'UGC05721':7,'UGC05750':8,'UGC05764':10,
    'UGC05829':10,'UGC05918':10,'UGC05986':9,'UGC05999':10,'UGC06399':9,
    'UGC06446':7,'UGC06614':1,'UGC06628':9,'UGC06667':6,'UGC06786':0,
    'UGC06787':2,'UGC06818':9,'UGC06917':9,'UGC06923':10,'UGC06930':7,
    'UGC06973':2,'UGC06983':6,'UGC07089':8,'UGC07125':9,'UGC07151':6,
    'UGC07232':10,'UGC07261':8,'UGC07323':8,'UGC07399':8,'UGC07524':9,
    'UGC07559':10,'UGC07577':10,'UGC07603':7,'UGC07608':10,'UGC07690':10,
    'UGC07866':10,'UGC08286':6,'UGC08490':9,'UGC08550':7,'UGC08699':2,
    'UGC08837':10,'UGC09037':6,'UGC09133':2,'UGC09992':10,'UGC10310':9,
    'UGC11455':6,'UGC11557':8,'UGC11820':9,'UGC11914':2,'UGC12506':6,
    'UGC12632':9,'UGC12732':9,'UGCA281':11,'UGCA442':9,'UGCA444':10,
}

MORPHOLOGY_LABEL = {
    0:'S0', 1:'Sa', 2:'Sab', 3:'Sb', 4:'Sbc', 5:'Sc',
    6:'Scd', 7:'Sd', 8:'Sdm', 9:'Sm', 10:'Im', 11:'BCD'
}


def load_sparc(filepath):
    """
    Load SPARC mass model file into a DataFrame.

    Parameters
    ----------
    filepath : str or Path
        Path to MassModels_Lelli2016c.txt or equivalent.

    Returns
    -------
    df : pd.DataFrame
        Columns: Galaxy, r, V_obs, eV, V_gas, V_disk, V_bul, SB_disk, SB_bul
        All velocities in km/s, r in kpc, SB in L_sun/pc^2.
    """
    rows = []
    with open(filepath) as f:
        for line in f:
            if line.startswith('#') or line.strip() == '':
                continue
            p = line.split()
            if len(p) < 9:
                continue
            try:
                rows.append({
                    'Galaxy':   p[0],
                    'r':        float(p[2]),
                    'V_obs':    float(p[3]),
                    'eV':       float(p[4]),
                    'V_gas':    float(p[5]),
                    'V_disk':   float(p[6]),
                    'V_bul':    float(p[7]),
                    'SB_disk':  float(p[8]),
                    'SB_bul':   float(p[9]) if len(p) > 9 else 0.0,
                })
            except (ValueError, IndexError):
                continue

    df = pd.DataFrame(rows)
    df['T']    = df['Galaxy'].map(HUBBLE_TYPE).fillna(-1).astype(int)
    df['morph'] = df['T'].map(MORPHOLOGY_LABEL).fillna('Unknown')
    return df


def get_galaxy(df, name):
    """
    Extract valid rotation curve points for a single galaxy.

    Applies quality cuts: V_obs > 1 km/s, eV > 0, r > 0.

    Returns
    -------
    sub : pd.DataFrame, sorted by r.
    """
    sub = df[df['Galaxy'] == name].copy()
    sub = sub[(sub['V_obs'] > 1) & (sub['eV'] > 0) & (sub['r'] > 0)]
    return sub.sort_values('r').reset_index(drop=True)


def galaxy_list(df):
    """Return sorted list of unique galaxy names."""
    return sorted(df['Galaxy'].unique())


def morphology_groups(df):
    """
    Return dict mapping group label to list of galaxy names.

    Groups:
        'early'  : T in [0, 1, 2]  S0–Sab
        'disk'   : T in [3, 4, 5, 6, 7]  Sb–Sd
        'irreg'  : T in [8, 9, 10, 11]  Sdm–Im–BCD
    """
    groups = {'early': [], 'disk': [], 'irreg': []}
    for gname in galaxy_list(df):
        T = HUBBLE_TYPE.get(gname, -1)
        if T <= 2:
            groups['early'].append(gname)
        elif T <= 7:
            groups['disk'].append(gname)
        else:
            groups['irreg'].append(gname)
    return groups
