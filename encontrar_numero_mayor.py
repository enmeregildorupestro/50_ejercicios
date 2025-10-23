for i in range(10):
    n = float(input(f"Ingrese el número {i+1}: "))
    numeros.append(n) # type: ignore

print(f"El número mayor es: {max(numeros)}") # type: ignore