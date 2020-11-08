a =[]
b=[]
festa=True
n=int(input())
while True:
    try:
        x,y=input().split()
        if x in a and y not in b and y not in a:
            b.append(y)
        elif x not in a and x not in b and y in b:
            a.append(x)
        elif x in b and y not in a and y not in b:
            a.append(y)
        elif x not in b and not x in a and y in a:
            b.append(x)
        elif x not in a and x not in b and y not in a and y not in b:
            a.append(x)
            b.append(y)
        else:            
            festa = False
                
    except EOFError:
        break
if festa == True:
    print("FESTA!")
else:
    print("Lascou...")
