def creaArray(num):
    numStr=str(num)
    array=[]
    for n in numStr:
        numeroInt=int(n)
        array.append(numeroInt)
    return array


arregloMayor=[1]
for x in range(100,1000):
    for z in range(100,1000):
        numero=x*z
        arreglo=creaArray(numero)
        if(len(arreglo))==5:
            if(arreglo[0]==arreglo[4] and arreglo[1]==arreglo[3] and arreglo[0]>arregloMayor[0] and len(arreglo)>len(arregloMayor)):
                arregloMayor=arreglo
        elif(len(arreglo)==6):
            if (arreglo[0] == arreglo[5] and arreglo[1] == arreglo[4] and arreglo[2]==arreglo[3] and arreglo[0]>arregloMayor[0]):
                arregloMayor=arreglo
print(arregloMayor)
