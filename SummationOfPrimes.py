def esPrimo(numero):
    for i in range(2,numero):
            if ((numero%i)==0):
                return False
    return True

suma = 0
for i in range(2, 2000001):
    if (esPrimo(i)):
        suma += i
print(suma)

#NO TERMINA DE EJECUTAR NUNCA -.- HAY QUE BUSCAR UNA SOLUCION MAS EFICIENTE