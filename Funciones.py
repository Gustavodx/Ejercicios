def saludar():
    print('Hola mundo! ')

def calcularDoble(num):
    res= num*2
    print(res)

def triplicar(num):
    res= num*3
    print(res)

# proceso principal, que invoca a las funciones antes declaradas
def menu():
    print('Llamada a la funcion Saludar: " ')   
    saludar()
    num= int (input("Ingrese un valor numerico para x: "))
    print('Llamada a la funcion CalcularDoble: " ')  
    print('El doble de',num,'es: ')
    calcularDoble(num)
    print('El valor original de x es: ',num)
    print('Llamada a la funcion Triplicar')  
    print('El nuevo valor de',num, 'es: ') 
    triplicar(num) 

menu()