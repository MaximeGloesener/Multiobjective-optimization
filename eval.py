"""
Comparaison des solutions obtenues avec celles des autres étudiants
"""
from utils import hypervolume, domine


# Trouve le nombre de solutions dominées par une autre solution
def number_dominated(sol1, sol2):
    number = 0
    same = 0
    for sc in sol1:
        for sc2 in sol2:
            if sc == sc2:
                same += 1
            # si score 1 dominé alors compteur + 1 et on passe au prochain score du jeu 1
            if domine(sc2, sc):
                number += 1
                break
    return number, same

# Comparer les solutions
def compare(filenameA, filenameB):
    with open(filenameA, 'r') as f1, open(filenameB, 'r') as f2:
        n1 = f1.readline()
        n2 = f2.readline()
        data1 = [tuple(map(int, line.strip().split())) for line in f1]
        data2 = [tuple(map(int, line.strip().split())) for line in f2]
        domine1, same = number_dominated(data1, data2)
        domine2, same = number_dominated(data2, data1)
    ref = [max(idx)*1.1 for idx in zip(*data1)]
    print(f"Nombre de solutions de A = {len(data1)}")
    print(f"Nombre de solutions de B = {len(data2)}")
    print(f"Nombre de solutions identiques : {same}")
    print(f"Nombre de solutions dominées dans A par B = {domine1}")
    print(f"Nombre de solutions dominées dans B par A = {domine2}")
    print(
        f"Nombre de solutions non dominées dans A par B = {len(data1)-domine1}"
    )
    print(
        f"Nombre de solutions non dominées dans B par A = {len(data2)-domine2}"
    )

compare("Data/solutions/30/30_15minutes.txt","Data/solutions/autres/30/tom.txt")
