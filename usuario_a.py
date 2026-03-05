def fibonacci(n):
    """
    Recibe un número entero n y devuelve una lista
    con los primeros n términos de la serie Fibonacci.
    """
    if n <= 0:
        return []

    serie = []

    a, b = 0, 1

    for _ in range(n):
        serie.append(a)
        a, b = b, a + b

    return serie

def es_capicua(numero):
    """
    Recibe un número entero y devuelve True si es capicúa,
    o False si no lo es.
    """
    numero_str = str(numero)
    return numero_str == numero_str[::-1]

def es_numero_perfecto(numero):
    """
    Recibe un número entero y devuelve True si es perfecto,
    o False si no lo es.
    """
    return