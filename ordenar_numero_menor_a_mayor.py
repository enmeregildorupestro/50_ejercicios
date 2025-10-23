for i in range(5):
    n = float(input(f"Ingrese el número {i+1}: "))
    numeros.append(n) # type: ignore

numeros.sort() # type: ignore
print("Números ordenados:", numeros) # type: ignore