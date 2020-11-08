n = int(input())
esq = {}
direita = {}
for i in range(n):
    e,d = input().split()
    if e in esq:
        esq[e] += 1
    else:
        esq[e] = 1
    if d in direita:
        direita[d] += 1
    else:
        direita[d] = 1
x = dict((k, v) for k, v in esq.items() if v > 1)
y = dict((k, v) for k, v in direita.items() if v > 1)
esq=sorted(list(map(int,x.keys())))
direita=sorted(list(map(int,y.keys())))

maximo = max([len(esq),len(direita)])
for i in range(maximo):
    if len(esq) > i and len(direita) > i:
        if esq[i] < direita[i]:
            print("%d E %d" %(esq[i],x[str(esq[i])]-1))
            print("%d D %d" %(direita[i],y[str(direita[i])]-1))
        else:
            print("%d D %d" %(direita[i],y[str(direita[i])]-1))
            print("%d E %d" %(esq[i],x[str(esq[i])]-1))
    elif len(direita) > i:
        print("%d D %d" %(direita[i],y[str(direita[i])]-1))
    else:
        print("%d E %d" %(esq[i],x[str(esq[i])]-1))
if maximo == 0:
    print("SEM TROCAS DESTA VEZ")

        
    
