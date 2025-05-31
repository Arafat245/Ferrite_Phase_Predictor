
import numpy as np
import pandas as pd

def sc_calc(C, N, Mn, Ni, Cr, Mo, Si, Cu, Nb):
    
    
    Nieq = Ni + 30*C + 0.5*Mn
    Creq = Cr + Mo + 1.5*Si

    # print(f'According to Schaffler Nieq: {Nieq}')
    # print(f'According to Schaffler Creq: {Creq}')
    
    def ferrite_sc(Nieq, Creq, a, b):
        return a*((Nieq+2) / (Creq-5.4)) + b

    data_sc = {
    "a": [-55.6, -41.7, -64.5, -190.5, -296.3, -121.2],
    "b": [60.6, 46.7, 66.8, 158.1, 223.7, 138.8],
    "FE (vol%) min": [0, 5, 10, 20, 40, 80],
    "FE (vol%) max": [5, 10, 20, 40, 80, 100]
    }

    abdata_sc = pd.DataFrame(data_sc)
    
    for index, row in abdata_sc.iterrows():
        fe_sc = ferrite_sc(Nieq, Creq, row['a'], row['b'])
        fe_sc = int(fe_sc)

        if row['FE (vol%) min'] <= fe_sc and fe_sc <= row['FE (vol%) max']:
            return fe_sc
    return 0
    
    
    
