def generar_secuencia_bn(n_terminos):
    """Genera la secuencia bn = (-1)^n"""
    return [(-1)**n for n in range(n_terminos)]

def generar_secuencia_cn(n_terminos):
    """Genera la secuencia cn = 2*5^n"""
    return [2 * (3**n) for n in range(n_terminos)]

def generar_secuencia_dn(n_terminos):
    """Genera la secuencia dn = 6*(1/3)^n"""
    return [6 * (1/3)**n for n in range(n_terminos)]

def mostrar_secuencia(nombre, secuencia, formato=""):
    """Muestra la secuencia con formato específico"""
    print(f"\nSecuencia {nombre}:")
    if formato == "fraccion":
        # Para la secuencia dn, mostrar como fracciones
        terminos = []
        for num in secuencia:
            if num >= 1:
                terminos.append(str(num))
            else:
                # Convertir decimales a fracciones simples
                denominador = 3 ** (len(str(num).split('.')[-1]))
                numerador = int(num * denominador)
                terminos.append(f"{numerador}/{denominador}")
    else:
        terminos = [str(num) for num in secuencia]
    
    print(", ".join(terminos))

def main():
    # Número de términos a generar
    n_terminos = 5
    
    print("Generando las tres secuencias geométricas:")
    print("-" * 50)
    
    # Generar y mostrar secuencia bn
    secuencia_bn = generar_secuencia_bn(n_terminos)
    mostrar_secuencia("bn = (-1)^n", secuencia_bn)
    
    # Generar y mostrar secuencia cn
    secuencia_cn = generar_secuencia_cn(n_terminos)
    mostrar_secuencia("cn = 2*3^n", secuencia_cn)
    
    # Generar y mostrar secuencia dn
    secuencia_dn = generar_secuencia_dn(n_terminos)
    mostrar_secuencia("dn = 6*(1/3)^n", secuencia_dn, formato="fraccion")
    
    # Mostrar información adicional
    print("\nInformación de las secuencias:")
    print("-" * 50)
    print("Secuencia bn: término inicial = 1, razón = -1")
    print("Secuencia cn: término inicial = 2, razón = 5")
    print("Secuencia dn: término inicial = 6, razón = 1/3")

if __name__ == "__main__":
    main()