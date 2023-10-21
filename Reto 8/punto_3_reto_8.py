n = int(input("Ingrese un número natural que sea mayor o igual a 2")) # Pedir un número 
if n >=2: # Sí n es mayor o igual que n
    if n % 2 == 0: # Sí n es par
        for numero in range(n, 1, -2): # Desde n hasta 1, saltando en 2 (8, 6, 4, 2)
            print(numero) 
    else: # Sí n no es par
        for numero in range(n-1, 1, -2): # Desde n-1, para que el número sea par, hasta 1, saltando en 2 (8, 6, 4, 2)
            print(numero)
else: # El número solo puede ser mayor o igual que cero
    print("Ingrese un número natural que sea mayor o igual a 2")