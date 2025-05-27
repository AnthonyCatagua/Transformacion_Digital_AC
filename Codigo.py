def calcular_promedio(lista_numeros):
    """
    Calcula el promedio de una lista de números.
    
    Args:
        lista_numeros (list): Una lista de números enteros o decimales
    
    Returns:
        float: El promedio de los números en la lista
    
    Raises:
        ValueError: Si la lista está vacía
        TypeError: Si la lista contiene elementos no numéricos
    """
    if not lista_numeros:
        raise ValueError("La lista está vacía")
    
    if not all(isinstance(x, (int, float)) for x in lista_numeros):
        raise TypeError("Todos los elementos deben ser números")
    
    return sum(lista_numeros) / len(lista_numeros)

# Ejemplo de uso
try:
    numeros = [10, 20, 30, 40, 50]
    resultado = calcular_promedio(numeros)
    print(f"El promedio es: {resultado}")
except (ValueError, TypeError) as error:
    print(f"Error: {error}")