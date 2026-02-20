def inclusion_exclusion(M, E, P, ME, MP, EP, MEP):
    # Aplicamos la fórmula de inclusión y exclusión
    total_students = M + E + P - ME - MP - EP + MEP

    # Mostramos los cálculos paso a paso
    print(f"|M| = {M}, |E| = {E}, |P| = {P}")
    print(f"|M ∩ E| = {ME}, |M ∩ P| = {MP}, |E ∩ P| = {EP}")
    print(f"|M ∩ E ∩ P| = {MEP}")
    print("\nAplicando la fórmula de Inclusión y Exclusión:")
    print(f"|M ∪ E ∪ P| = {M} + {E} + {P} - {ME} - {MP} - {EP} + {MEP}")
    print(f"Resultado: {total_students}")

    return total_students

# Datos del problema
M = 60   # Estudiantes de Matemáticas
E = 200  # Estudiantes de EECS
P = 40   # Estudiantes de Física
ME = 4 + 2   # Doble especialización en Matemáticas y EECS
MP = 3 + 2   # Doble especialización en Matemáticas y Física
EP = 11 + 2  # Doble especialización en EECS y Física
MEP = 2      # Triple especialización

# Llamamos a la función
total = inclusion_exclusion(M, E, P, ME, MP, EP, MEP)

# Output final
print(f"\nNúmero total de estudiantes en los departamentos: {total}")
