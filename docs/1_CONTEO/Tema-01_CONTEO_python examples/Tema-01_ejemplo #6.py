def calcular_probabilidad_moneda():
    # Probabilidad de cara en el primer lanzamiento
    P_A = 1/2
    print(f"P(A) = Probabilidad de cara en primer lanzamiento = {P_A}")
    
    # Probabilidad de cara en el último lanzamiento
    P_B = 1/2
    print(f"P(B) = Probabilidad de cara en último lanzamiento = {P_B}")
    
    # Probabilidad de cara en ambos lanzamientos (intersección)
    P_AB = 1/2 * 1/2  # Eventos independientes
    print(f"P(A∩B) = Probabilidad de cara en ambos lanzamientos = {P_AB}")
    
    # Aplicando principio de inclusión-exclusión
    P_AUB = P_A + P_B - P_AB
    print(f"\nP(A∪B) = P(A) + P(B) - P(A∩B)")
    print(f"P(A∪B) = {P_A} + {P_B} - {P_AB}")
    print(f"P(A∪B) = {P_AUB}")
    print(f"\nLa probabilidad es {P_AUB:.2%}")
    
    return P_AUB

# Ejecutar el cálculo
if __name__ == "__main__":
    print("Calculando la probabilidad de obtener cara en el primer O último lanzamiento...")
    print("-" * 70)
    resultado = calcular_probabilidad_moneda()
