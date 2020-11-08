n,p = map(int,input().split())
partidos = []
for i in range(p):
    partidos.append(int(input()))
q = round(sum(partidos)/n)
print("%d %d" %(sum(partidos), q))
x = []
for i in range(p):
    x.append(partidos[i]//q)
remanescente = n - sum(x)
while remanescente != 0:
    maximo = 0
    partido = -1
    for i in range(p):
        if x[i] != 0:
            media = partidos[i]/(x[i]+1)
            if media > maximo:
                partido = i
                maximo = media
    x[partido]+=1
    remanescente -=1
    
for i in range(p):
    print("Partido %d: %d" %(i+1,x[i]))
