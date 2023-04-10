import sys

def reverse_case(string):
    """
    Funcion que invierte y cambia mayus y minus de un string
    """
    return string.swapcase()[::-1]

# Verificar si se proporcionaron argumentos
if len(sys.argv) > 1:
    # Combinar los argumentos en un solo string separado por un espacio
    args = ' '.join(sys.argv[1:])
    # Aplicar la función reverse_case al string combinado
    result = reverse_case(args)
    # Imprimir el resultado
    print(result)
else:
    # Si no se proporcionaron argumentos, imprimir un mensaje de uso
    print("Usage: python3 exec.py <string>")
