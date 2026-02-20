# n! Factorial de n
# ---
from math import factorial

def fac(n):
    result = 1
    for i in range(1, n+1):
        result *= i     
    return result

n = int(input('Ingresa un número: '))
print(f'El calculo de la factorial de {n}! es {fac(n)}')

print(f'Resultado de la función matemática de factorial de {n}! es {factorial(n)}')

