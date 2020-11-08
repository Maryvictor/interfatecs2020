while True:
    try:
        n=int(input())
        idades=[]
        for i in range(n):
            idade= int(input())
            idades.append(idade)
        idades.sort()
        media = sum(idades)/n
        if n%2 == 1:
            mediana = idades[(n+1)//2-1]
        else:
            mediana = (idades[n//2]+idades[(n//2)-1])/2
        modes = []
        number_counts = {}
        for i in idades:
            if i in number_counts:
                number_counts[i] += 1
            else:
                number_counts[i] = 1
        for i in number_counts:
            most_values = max(number_counts.values())
        for key, value in number_counts.items():
            if  most_values == value:
                modes.append(key)
        
        moda = (",").join(map(str,modes))
        print("MODA=%s" %moda)
        print("MEDIA=%.2f" %media)
        print("MEDIANA=%.2f" %mediana)
    except:
        break


