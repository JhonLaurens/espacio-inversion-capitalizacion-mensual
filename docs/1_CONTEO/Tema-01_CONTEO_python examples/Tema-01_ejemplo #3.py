def contar_selecciones():
    # Cantidad de libros en cada categoría
    computacion = 5
    matematicas = 3
    arte = 2
    
    # Calcular diferentes libros posibles
    libros_cm = computacion * matematicas # Computación y Matemáticas
    libros_ca = computacion * arte        # Computación y Arte
    libros_ma = matematicas * arte        # Matemáticas y Arte
    
    # Sumar todas las posibildades de diferentes libros
    total_libros = libros_cm + libros_ca + libros_ma
    
    return total_libros

# Ejecutar la función e imprimir el resultado
print("Total de maneras de seleccionar dos libros de temas diferentes:", contar_selecciones())