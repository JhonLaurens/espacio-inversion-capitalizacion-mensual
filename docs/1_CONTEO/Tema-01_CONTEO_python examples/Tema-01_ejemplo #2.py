def contar_cadenas():
    # Definir la cantidad de bits libres después del prefijo
    bits_libres = 5  # 8 bits totales - 3 bits fijos
    
    # Calcular las diferentes cadenas posibles para cada prefijo
    cadenas_101 = 2 ** bits_libres
    cadenas_111 = 2 ** bits_libres
    
    # Sumar ambos casos (no hay intersección)
    total_cadenas_101y111 = cadenas_101 + cadenas_111
    
    return total_cadenas_101y111

# Ejecutar la función e imprimir el resultado
print("Total de cadenas de ocho bits que comienzan con 101 o 111:", contar_cadenas())