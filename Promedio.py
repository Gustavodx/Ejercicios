num = int(input("Ingrese la cantidad de datos: "))
acum =0

for i in range(1 , num+1):
    dato = int(input("Ingrese el numero: "))
    acum = acum+dato

prom = acum/num

print( 'El promedio es: ', prom)
