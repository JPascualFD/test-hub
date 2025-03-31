nombre = "Soy el desarrollador Pan de melon !"
apellido = "Sanchez"

saludo = "Hola " + nombre + " " + apellido + " come torta?"

def x(parametro):
    """
    Función 'x' que realiza una operación específica.
    :param parametro: Valor de entrada (puede ser cualquier tipo).
    :return: Resultado procesado.
    """
    resultado = parametro * 2  # Ejemplo: duplica el parámetro
    return resultado

# Ejemplo de uso
print(x(5))  # Salida: 10

def es_par(numero):
    """Verifica si un número es par."""
    return numero % 2 == 0

# Ejemplo de uso
print(es_par(4))  # Salida: True
print(es_par(7))  # Salida: False

print(saludo)