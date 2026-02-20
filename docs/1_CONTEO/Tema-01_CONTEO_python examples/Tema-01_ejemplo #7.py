def generar_secuencia_sn(n_terminos):
    """
    Genera la secuencia sn = -1 + 4n
    Parámetros:
    n_terminos: número de términos a generar
    """
    return [-1 + 4*n for n in range(n_terminos)]

def generar_secuencia_tn(n_terminos):
    """
    Genera la secuencia tn = 2 + 3n
    Parámetros:
    n_terminos: número de términos a generar
    """
    return [2 + 3*n for n in range(n_terminos)]

def mostrar_secuencia(nombre, secuencia, formula, termino_inicial, diferencia):
    """
    Muestra la información detallada de una secuencia
    """
    print(f"\nSecuencia {nombre}:")
    print(f"Fórmula: {formula}")
    print(f"Término inicial: {termino_inicial}")
    print(f"Diferencia común: {diferencia}")
    print(f"Primeros {len(secuencia)} términos: {', '.join(map(str, secuencia))}")
    
def generar_string_binario(longitud):
    """
    Ejemplo de generación de string binario
    """
    from random import choice
    return ''.join(choice(['0', '1']) for _ in range(longitud))

def main():
    # Número de términos a generar
    n_terminos = 10
    
    print("Análisis de Secuencias Aritméticas")
    print("=" * 50)
    
    # Generar y mostrar secuencia sn
    secuencia_sn = generar_secuencia_sn(n_terminos)
    mostrar_secuencia(
        "sn",
        secuencia_sn,
        "sn = -1 + 4n",
        termino_inicial=-1,
        diferencia=4
    )
    
    # Generar y mostrar secuencia tn
    secuencia_tn = generar_secuencia_tn(n_terminos)
    mostrar_secuencia(
        "tn",
        secuencia_tn,
        "tn = 2 + 3n",
        termino_inicial=2,
        diferencia=+3
    )
    
    # Ejemplos de strings
    print("\nEjemplos de Strings en Informática")
    print("=" * 50)
    print("String vacío (λ):", "")
    print("Longitud del string vacío:", 0)
    
    # Ejemplo con string binario
    bit_string = generar_string_binario(8)
    print(f"\nEjemplo de bit string de longitud 8: {bit_string}")
    print(f"Longitud del bit string: {len(bit_string)}")

if __name__ == "__main__":
    main()