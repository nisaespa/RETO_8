import math  # Importar math para usar funcion exponencial
# Función para calcular la aproximación exponencial
def exponencial(x, n):
    aproximacion = 0
    for i in range(n): # Iterar n veces
        termino = (x ** i) / math.factorial(i)  # Calcula un término de la serie de Maclaurin
        aproximacion += termino  # suma el término a la aproximación
    valor_real = math.exp(x)  # Calcula el valor real usando math.exp()
    diferencia = abs(valor_real - aproximacion)  # Calcular la resta entre el valor real y la aproximación
    return aproximacion, diferencia  # retorna la aproximación y la diferencia
# Iniciar programa
if __name__ == '__main__':
    x = float(input("Escriba un número real: "))  # Pedir número real
    error = 0.001  # Establece el error para la aproximación 
    n = 0  # Inicializa un contador para el número de términos en la serie
    while True: # Iniciar bucle infinito
        n += 1  # Incrementa el contador en cada iteración
        aproximacion, diferencia = exponencial(x, n)  # Pasar la función a dos variables
        if diferencia < error:  # Sí la diferencia es menor que el error
            break  # Sale del bucle hasta que la diferencia sea igual que el error
    print(f"La aproximación es: {aproximacion}") 
    print(f"El valor real es: {math.exp(x)}")  
    print(f"La diferencia es: {diferencia}")  
    print(f"Valor de n necesario para un error menor al {error}%: {n}")  