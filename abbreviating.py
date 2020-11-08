

def qsort(inlist):
    if inlist == []: 
        return []
    else:
        pivot = inlist[0]
        lesser = qsort([x for x in inlist[1:] if x < pivot])
        greater = qsort([x for x in inlist[1:] if x >= pivot])
        return lesser + [pivot] + greater

nomes = []
while True:
    try:
        nome = input().split()
        for i in range(1, len(nome)-1):
            nome[i] = nome[i][0]+"."
        nomes.append(" ".join(nome))
    except EOFError:
        break

nomes = qsort(nomes)
for i in range(len(nomes)):
    print(nomes[i])
