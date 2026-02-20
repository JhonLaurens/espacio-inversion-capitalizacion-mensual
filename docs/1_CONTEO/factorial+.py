def fac(n):
    """Calcula el factorial de un número."""
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

while True:
    n = input('Ingresa un número (o Q/q/X/x para salir): ')
    if n.upper() in ['Q', 'X']:
        break
    try:
        n = int(n)
        print(f'El factorial de {n}! es {fac(n)}')
    except ValueError:
        print("Entrada inválida. Por favor, ingresa un número o Q/q/X/x para salir.")