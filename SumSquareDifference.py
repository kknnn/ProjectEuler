sumaDeCuadrados=0
cuadradoDeLaSuma=0
for i in range (1,101):
    sumaDeCuadrados+=i*i
for i in range(1,101):
    cuadradoDeLaSuma+=i
cuadradoDeLaSuma=cuadradoDeLaSuma*cuadradoDeLaSuma
print(cuadradoDeLaSuma-sumaDeCuadrados)