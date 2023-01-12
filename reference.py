"""
Fichier qui permet de trouver le point de référence commun à tous les groupes
"""

import os 

ref_tot = [0,0,0,0]
path = 'Data/solutions/autres/30'
for sol in os.listdir(path):
    with open(path+'/'+sol, 'r') as f1:
        n1 = f1.readline()
        data1 = [tuple(map(int, line.strip().split())) for line in f1]
        ref = [max(idx)*1.1 for idx in zip(*data1)]
    ref_tot = [round(max(idx),3) for idx in zip(ref, ref_tot)]

print(ref_tot)

