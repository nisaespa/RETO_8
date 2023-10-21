import math # Importar math para utilizar la función factorial
n = int(input("Ingrese un número natural")) # Pedir un número 
for numero in range(1, n + 1): # Iterar desde 1 hasta n + 1
    factorial = math.factorial(numero) # Utilizamos la función factorial
    print(f"El número es {numero} y su factorial es {factorial}") # Imprimir el número con su factorial