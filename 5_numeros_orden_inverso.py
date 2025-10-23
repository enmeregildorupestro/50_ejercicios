from unicodedata import numeric


for i in range(10):
    n = float(input(f"Ingrese el número {i+1}: "))
    numero.append(n) # type: ignore

print(f"El número mayor es: {max(numero)}") # type: ignore