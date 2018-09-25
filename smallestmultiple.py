masChico=0
numero=1
while(masChico==0):
    contador=0
    bandera=True
    i=1
    while(i<21 and bandera==True):
        if(numero%i!=0):
            bandera=False
        else:
            i=i+1
    if(bandera==True):
        masChico=numero
    else:
        numero=numero+1
print(masChico)
