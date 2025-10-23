notas = []

for i in range(5):
    nota = float(input(f"Ingrese la nota {i+1}: "))
    notas.append(nota)

promedio = sum(notas) / len(notas)
print(f"Promedio: {promedio}")
print(f"Nota mayor: {max(notas)}")
print(f"Nota menor: {min(notas)}")