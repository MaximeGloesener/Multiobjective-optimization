from utils import domine
fileA = 'merge2.txt'

def check(data, val1):
    for val in data:
        if domine(val, val1):
            return False 
    return True 


with open(fileA, 'r') as fin, open('merge3.txt', 'w') as fout:
    data =  set([tuple(map(int, line.strip().split())) for line in fin])
    sols = []

    for v in data:
        if check(data, v):
            sols.append(v)

    for sol in sols:
        fout.write(" ".join(str(int(i)) for i in sol) + "\n")

