import random
numero = random.randint(1, 100)
intentos = 0

print("Adivina el número (entre 1 y 100):")

while True:
    intento = int(input("Tu número: "))
    intentos += 1

    if intento == numero:
        print(f"¡Correcto! Lo lograste en {intentos} intentos.")
        break
    elif intento < numero:
        print("Demasiado bajo.")
    else:
        print("Demasiado alto.")