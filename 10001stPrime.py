def esPrimo(numero):
    divisores=[]
    for i in range(1,numero+1):
        if(numero%i==0):
            divisores.append(i)
    if(len(divisores)==2):
        return True
    else:
        return False

primos=[2]
num=3
while (len(primos)<10002):
    if(esPrimo(num)):
        primos.append(num)
    num+=1
print(primos[10000])

#104743