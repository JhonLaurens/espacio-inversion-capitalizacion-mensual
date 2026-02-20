from itertools import permutations

# Lista de personas
personas = ["Alicia", "Benjamín", "Consuelo", "Adolfo", "Eduardo", "Francisco"]

# a) Número total de maneras de seleccionar presidente, secretario y tesorero
def parte_a():
    # Generar todas las permutaciones de 3 personas
    todas_las_permutaciones = list(permutations(personas, 3))
    # El número de permutaciones es la respuesta
    return len(todas_las_permutaciones)

# b) Número de maneras si Alicia o Benjamín debe ser el presidente
def parte_b():
    contador = 0
    # Generar todas las permutaciones de 3 personas
    for perm in permutations(personas, 3):
        # Verificar si el presidente es Alicia o Benjamín
        if perm[0] in ["Alicia", "Benjamín"]:
            contador += 1
    return contador

# c) Número de maneras si Eduardo debe ocupar uno de los puestos
def parte_c():
    contador = 0
    # Generar todas las permutaciones de 3 personas
    for perm in permutations(personas, 3):
        # Verificar si Eduardo está en la permutación
        if "Eduardo" in perm:
            contador += 1
    return contador

# d) Número de maneras si Adolfo y Francisco deben ocupar un puesto
def parte_d():
    contador = 0
    # Generar todas las permutaciones de 3 personas
    for perm in permutations(personas, 3):
        # Verificar si Adolfo y Francisco están en la permutación
        if "Adolfo" in perm and "Francisco" in perm:
            contador += 1
    return contador

# Mostrar resultados
print("Personas del comité: ", personas)
print("a) Número total de maneras:", parte_a())
print("b) Maneras si Alicia o Benjamín es presidente:", parte_b())
print("c) Maneras si Eduardo ocupa un puesto:", parte_c())
print("d) Maneras si Adolfo y Francisco ocupan un puesto:", parte_d())