# Definir las opciones del menú
entremes = ["N", "S"]  # Nachos, Salami
platos_fuertes = ["H", "C", "F"]  # Hamburgesa, Carne, Filete
bebidas = ["T", "M", "C", "R"]   # Té, Malteada, Cerveza, Refresco

#1 Generar todas las comidas posibles de un plato fuerte con una bebida
comidas_1 = [pf + b for pf in platos_fuertes for b in bebidas]

#2 Generar todas las comidas posibles con los tres platos
comidas_2 = [e + pf + b for e in entremes for pf in platos_fuertes for b in bebidas]

# Mostrar resultados de comidas diferentes y la cantidad total posible
print("Comidas posibles con plato fuerte y bebidas:", comidas_1)
print("Total de comidas con los tres platos:", len(comidas_2))
