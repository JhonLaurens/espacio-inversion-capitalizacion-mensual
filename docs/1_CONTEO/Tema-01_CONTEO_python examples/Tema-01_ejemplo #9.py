from itertools import permutations, combinations
from math import factorial, comb

personas = ["Ana", "Juan", "Pedro", "Luis", "María"]

def permutaciones(n, r):
    return factorial(n) // factorial(n - r)    

def permutar(r):
    for p in permutations(personas, r):
        print(p)
    return 

def combinaciones(n, r):
    return {comb(n, r)}   

def combinaciones_formula(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))  

def combinar(r):
    for c in combinations(personas, 3):
        print(c)
    return  


# Ejecutar el cálculo
if __name__ == "__main__":
    # Permutaciones de 3 lugares de 5 personas posibles (orden importa)
    print("Permutaciones (el orden importa).")
    print(f'Se tienen {permutaciones(3, 3)} posibles permutaciones para 3 lugares de las 5 personas posibles:')
    permutar(3)

    # Combinaciones de 3 lugares de 5 personas posibles (el orden NO importa)
    print("Combinaciones (el orden NO importa).")
    print(f'Se tienen {combinaciones(5, 3)} posibles combinaciones para 3 lugares de las 5 personas posibles:')
    combinar(3)
    print(f'Se tienen por fórmula {combinaciones_formula(5, 3)} posibles combinaciones para 3 lugares de las 5 personas posibles:')