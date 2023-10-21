n = int(input("Ingrese un número")) # Pedir un número 
for i in range(n, n + 1): # iterar una vez, con el valor de n
    potencia = 2 ** i # Formula para potencia con el valor de n
    print(f"2 elevado a {n} es: {potencia}") # Imprimir resultado
