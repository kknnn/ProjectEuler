def para10():
    numeros=[]
    numeros2=[]
    for i in range(1,11):
        numeros.append(i)
    for i in range (len(numeros)-1):
        if((numeros[i]%3)==0 or (numeros[i]%5)==0):
            numeros2.append(numeros[i])
    print(numeros)
    print(numeros2)
    print(sum(numeros2))

def para1000():
    numeros = []
    numeros2 = []
    for i in range(1, 1001):
        numeros.append(i)
    for i in range(len(numeros) - 1):
        if ((numeros[i] % 3) == 0 or (numeros[i] % 5) == 0):
            numeros2.append(numeros[i])
    print(numeros)
    print(numeros2)
    print(sum(numeros2))

para1000()