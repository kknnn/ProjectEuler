def cuantosDivisores(numero):
    divisores=[]
    for i in range(1,numero+1):
        if(numero%i==0):
            divisores.append(i)
        if(len(divisores)>500):
            break
    return len(divisores)

triangular=1
j=1
bandera=True
while(bandera):
    if(cuantosDivisores(triangular)>500):
        print(triangular)
        bandera=False
        break
    else:
        j+=1
        triangular+=j
