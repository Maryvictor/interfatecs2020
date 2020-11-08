
h,c,l= map(float,input().split())
while h != 0.0 and c != 0.0 and l != 0:
    if l >= 0.8 and h/c <= 0.08334:
        print("PROJETO SIMPLES")
    else:
        print("PROJETO ESPECIAL")
    h,c,l= map(float,input().split())
    
    
