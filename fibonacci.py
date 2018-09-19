#fibonacci=[]
#for i in range(1,11):
#    if(i==1):
#        fibonacci.append(i)
#    elif(i==2):
#        fibonacci.append(i)
#    else:
#        fibonacci.append(fibonacci[i-2]+fibonacci[i-3])
#print(fibonacci)
fibonacci=[]
mayor=0
i=1
while(mayor<4000000):
    if (i == 1):
        fibonacci.append(i)
        i=i+1
    elif(i==2):
        fibonacci.append(i)
        i = i + 1
    else:
        fibonacci.append(fibonacci[i-2]+fibonacci[i-3])
        mayor=fibonacci[i-1]
        i = i + 1
ultimo=len(fibonacci)
if(fibonacci[ultimo-1]>4000000):
    del fibonacci[ultimo-1]
#sumapares=0
#for i,valor in enumerate(fibonacci):
#    if(valor%2==0):
#        sumapares+=valor
#print(sumapares)

sumapares=0
for i in range(len(fibonacci)):
    if(fibonacci[i]%2==0):
        sumapares+=fibonacci[i]
print(sumapares)
print(fibonacci)