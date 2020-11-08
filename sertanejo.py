def qsort(inlist):
    if inlist == []: 
        return []
    else:
        pivot = inlist[0]
        lesser = qsort([x for x in inlist[1:] if x < pivot])
        greater = qsort([x for x in inlist[1:] if x >= pivot])
        return lesser + [pivot] + greater

def busca4(g, orig, dest, lim):
    if orig == dest: return True
    if lim == 1: return False
    if g[orig][dest] != 0: return True
    for i in range(len(g[orig])):
        if g[orig][i] != 0:
            if busca4(g, i, dest, lim-1): return True
    return False
def busca5(g, orig, dest):
    fila = []
    fila.append((orig, 1))
    while fila != []:
        v = fila.pop(0)
        if v[0] == dest: return v[1]
        if g[v[0]][dest] != 0: return v[1]+1
        for i in range(len(g[v[0]])):
            if g[v[0]][i] != 0: fila.append((i,v[1]+1))
    return 0
n = int(input())
grau = {}
duplas = [[0] * (n*2) for i in range(n*2)]
pessoas = {"Saracura":0}
pessoa = []
for i in range(n):
    x, y = input().split(" e ")
    if x not in pessoas:
        pessoas[x] = len(pessoas)
        pessoa.append(x)
    if y not in pessoas:
        pessoas[y] = len(pessoas)
        pessoa.append(y)
    duplas[pessoas[x]][pessoas[y]] = 1
    duplas[pessoas[y]][pessoas[x]] = 1
lista = []
for i in range(len(pessoa)):
    if busca4(duplas,0,pessoas[pessoa[i]],len(pessoa)) == False:
        lista.append([1000,pessoa[i]])
    else:
        resultado = busca5(duplas,0,pessoas[pessoa[i]])
        lista.append([resultado-1,pessoa[i]])
lista=qsort(lista)
for i in range(len(pessoa)):
    if lista[i][0] == 1000:
        lista[i][0] = "infinito"
    print("%s: %s" %(lista[i][1], str(lista[i][0])))
