from utils import domine
fileA = 'Data/solutions/20/20.txt'

def check(data, val1):
    for val in data:
        if domine(val, val1):
            return False 
    return True 


with open(fileA, 'r') as fin, open('20All.txt', 'w') as fout:
    data =  set([tuple(map(int, line.strip().split())) for line in fin])
    sols = []

    for v in data:
        if check(data, v):
            sols.append(v)

    for sol in sols:
        fout.write(" ".join(str(int(i)) for i in sol) + "\n")

