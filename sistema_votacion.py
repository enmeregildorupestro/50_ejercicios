candidatos = {"A": 0, "B": 0, "C": 0}

for i in range(5):  # puedes cambiar la cantidad de votantes
    voto = input("Vote por (A, B o C): ").upper()
    if voto in candidatos:
        candidatos[voto] += 1
    else:
        print("Voto no válido.")

ganador = max(candidatos, key=candidatos.get)
print("\nResultados:", candidatos)
print(f"Ganador: {ganador}")