import sys

def check_number(num):
    """
    Función que comprueba si un número es par, impar o cero
    """
    if num == 0:
        return "I'm Zero."
    elif num % 2 == 0:
        return "I'm Even."
    else:
        return "I'm Odd."

# Verificar si se proporcionó un argumento y si es un entero
if len(sys.argv) == 2 and sys.argv[1].isdigit():
    num = int(sys.argv[1])
    # Comprobar si el número es par, impar o cero
    result = check_number(num)
    # Imprimir el resultado
    print(result)
else:
    # Si no se proporcionó un argumento o no es un entero, imprimir un mensaje de error
    if len(sys.argv) == 1:
        print(" ")
    elif not sys.argv[1].isdigit():
        print("AssertionError: argument is not an integer")
    else:
        print("AsertionError: more than one argument are provided")
