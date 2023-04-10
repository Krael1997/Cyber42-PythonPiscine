import sys

# Verificar que se pase algun argumento
if len(sys.argv) < 3:
    print("Usage: python operations.py <number1> <number2>")
    print("Example: python operations.py 10 3")
    sys.exit(1)

# Verificar que se pasen dos argumentos enteros
try:
    a = int(sys.argv[1])
    b = int(sys.argv[2])
except (ValueError):
    print("AssertionError: only integers")
    sys.exit(1)

# Verificar que solo se pasen dos argumentos
if len(sys.argv) > 3:
    print("AssertionError: too many arguments")
    sys.exit(1)

# Realizar las operaciones
try:
    print("Sum:", a + b)
    print("Difference:", a - b)
    print("Product:", a * b)
    if b == 0:
        print("Quotient: ERROR (division by zero)")
        print("Remainder: ERROR (modulo by zero)")
    else:
        print("Quotient:", a / b)
        print("Remainder:", a % b)
except ZeroDivisionError:
    print("Quotient: ERROR (division by zero)")
    print("Remainder: ERROR (modulo by zero)")

