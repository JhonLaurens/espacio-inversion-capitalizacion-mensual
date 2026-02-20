import math

def catalan_number(n):
    return math.comb(2 * n, n) // (n + 1)

def generate_parenthesizations(n):
    if n == 0:
        return [""]
    result = []
    for i in range(n):
        for left in generate_parenthesizations(i):
            for right in generate_parenthesizations(n - 1 - i):
                result.append(f"({left}){right}")
    return result

# Solicitar al usuario el valor de n
n = int(input("Ingrese el valor de n: "))

# Calcular y mostrar el número de maneras de parentizar
print(f"Número de formas de parentizar {n} paréntesis: {catalan_number(n)}")
print("Formas posibles:")
for p in generate_parenthesizations(n):
    print(p)
