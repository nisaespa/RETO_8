n = int(input("Ingrese un número natural: ")) # Pedir un número natural
x = float(input("Ingrese un número real: ")) # Pedir un número real
potencia = 1 # Iniciarlizar en 1
for i in range(n): # Iterar n veces
    potencia *= x # Formula para potencia
print(f"{x} a la {n} es igual a : {potencia}") # Imprimir resultados