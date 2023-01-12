"""
Calcul la valeur des hypervolumes pour les solutions de tous les groupes 
"""
import os 
from utils import hypervolume

# Paramètres
ref = [225.5, 438.9, 636.9, 936.1]
path = 'Data/solutions/autres/30'

for sol in os.listdir(path):
    with open(path+'/'+sol, 'r') as f1:
        n1 = f1.readline()
        data1 = [tuple(map(int, line.strip().split())) for line in f1]
        print(path, hypervolume(ref, data1))