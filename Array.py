import random
a=[]

for i in range(1,11):
       x = random.randint(1,99)
       a.append(x) 

print("Los elementos del arreglo son: ")
print(a,"\n")
print("En orden Inverso: ")

for i in reversed(a):
    print(i, end=" ")
