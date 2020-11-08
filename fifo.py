n=int(input())
duracao = 0
tme = 0
tmt = 0
for i in range(n):
    c,d= map(int,input().split())
    tme += duracao-c
    duracao += d
    tmt += duracao-c
print("TME:%.1f" %(tme/n))
print("TMT:%.1f" %(tmt/n))
    

    
