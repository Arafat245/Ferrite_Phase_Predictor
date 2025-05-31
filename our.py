import numpy as np
import pandas as pd


def our_calc(C, N, Mn, Ni, Cr, Mo, Si, Cu, Nb):
    
    if C <= 0.08:
        # print('C less than 0.08')
        Nieq = Ni + 35*C + 20*N + 0.5*Mn + 0.25*Cu
        Creq = Cr + Mo + 0.7*Nb
    else:
        # print('C greater than 0.08')
        Nieq = Ni + 7*C + 7*N + 0.5*Mn + 0.25*Cu
        Creq = Cr + Mo + 0.7*Nb
        
    # print(f"According to Our Nieq = {Nieq}")
    # print(f"According to Our Creq = {Creq}")
        
        
    def ferrite_our(Nieq, Creq, a, b):
        return a*((Nieq+2) / (Creq-5.4)) + b

    data = {
    "a": [-55.6, -41.7, -64.5, -190.5, -296.3, -121.2],
    "b": [60.6, 46.7, 66.8, 158.1, 223.7, 138.8],
    "FE (vol%) min": [0, 5, 10, 20, 40, 80],
    "FE (vol%) max": [5, 10, 20, 40, 80, 100]
    }

    abdata = pd.DataFrame(data)
    
    for index, row in abdata.iterrows():
        fe_our = ferrite_our(Nieq, Creq, row['a'], row['b'])
        fe_our = int(fe_our)
        
        if row['FE (vol%) min'] <= fe_our and fe_our <= row['FE (vol%) max']:
            #print(f'According to Our Calculation Ferrite: {fe_our}')
            return fe_our,Nieq, Creq
    
    return 0,Nieq, Creq

            