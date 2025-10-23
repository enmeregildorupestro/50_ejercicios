for i in range(10):
    n = float(input(f"Ingrese el número {i+1}: "))
    numeros.append(n) # type: ignore

promedio = sum(numeros) / len(numeros) # type: ignore
print(f"El promedio es: {promedio}")