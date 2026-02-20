
def get_valid_number(prompt: str, type_func=float, min_val=None, max_val=None):
    """
    Solicita un número al usuario y valida que sea del tipo correcto y esté en el rango permitido.
    Inspirado en el patrón try-except de factorial+.py.
    
    Args:
        prompt: Mensaje para el usuario.
        type_func: Función de conversión (int o float).
        min_val: Valor mínimo permitido (opcional).
        max_val: Valor máximo permitido (opcional).
    
    Returns:
        El número validado.
    """
    while True:
        user_input = input(prompt)
        
        # Permitir salir con Q/X como en el ejemplo
        if user_input.upper() in ['Q', 'X']:
            return None
            
        try:
            val = type_func(user_input)
            
            if min_val is not None and val < min_val:
                print(f"Error: El valor debe ser mayor o igual a {min_val}.")
                continue
                
            if max_val is not None and val > max_val:
                print(f"Error: El valor debe ser menor o igual a {max_val}.")
                continue
                
            return val
            
        except ValueError:
            type_name = "entero" if type_func is int else "número"
            print(f"Entrada inválida. Por favor, ingresa un {type_name} válido.")
