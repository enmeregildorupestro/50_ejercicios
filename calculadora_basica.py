print("Operaciones: +, -, *, /")
op = input("Ingrese la operación: ")
a = float(input("Primer número: "))
b = float(input("Segundo número: "))

if op == '+':
    print(f"Resultado: {a + b}")
elif op == '-':
    print(f"Resultado: {a - b}")
elif op == '*':
    print(f"Resultado: {a * b}")
elif op == '/':
    print(f"Resultado: {a / b}")
else:
    print("Operación no válida.")