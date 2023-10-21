import math  # Importa math para seno y valor absoluto
def seno(x, n):
    aproximacion = 0  # Inicializa la variable 'aproximacion' a cero para acumular la suma de la serie
    for i in range(n):  # Itera n veces para calcular los términos de la serie de Maclaurin.
        termino = ((-1) ** i) * (x ** (2 * i + 1)) / math.factorial(2 * i + 1)  # Calcula cada término de la serie
        aproximacion += termino  # Sumar cada termino en la aproximación
    return aproximacion  # Devuelve la aproximación del seno
# Iniciar programa
if __name__ == '__main__':
    x = float(input("Ingresa un valor para x: "))  # Solicita al usuario que ingrese un número real
    n = 1
    error = 1 
    while error > 0.001:  # mientras el error sea mayor que 0.1
        seno_real = math.sin(x)  # Calcular el valor real del seno usando la función sin
        seno_aproximado = seno(x, n) # Pasar la función a dos variables
        error = abs(seno_real - seno_aproximado)  # Calcular el valor absoluto de la resta entre el valor real y la aproximación
        n += 1  # Incrementa 'n' para considerar más términos en la serie
    print(f"Se necesita n = {n} para tener un error menor o igual a 0.1%")
    print(f"Valor real del seno: {seno_real}")
    print(f"Aproximación del seno: {seno_aproximado}")
    print(f"Diferencia: {error}")
