a = []
b = []

print("Ingrese los 5 números del primer arreglo:")
for i in range(5):
    a.append(float(input(f"A[{i+1}]: ")))

print("Ingrese los 5 números del segundo arreglo:")
for i in range(5):
    b.append(float(input(f"B[{i+1}]: ")))

suma = [a[i] + b[i] for i in range(5)]
print("Suma de arreglos:", suma)