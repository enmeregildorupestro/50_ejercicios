saldo = float(input("Ingrese el saldo inicial: "))

while True:
    print("\n1. Consultar saldo")
    print("2. Consignar")
    print("3. Retirar")
    print("4. Salir")

    opcion = input("Elija una opción: ")

    if opcion == "1":
        print(f"Saldo actual: ${saldo:.2f}")
    elif opcion == "2":
        monto = float(input("Monto a consignar: "))
        saldo += monto
        print(f"Consignación exitosa. Nuevo saldo: ${saldo:.2f}")
    elif opcion == "3":
        monto = float(input("Monto a retirar: "))
        if monto > saldo:
            print("Saldo insuficiente.")
        else:
            saldo -= monto
            print(f"Retiro exitoso. Nuevo saldo: ${saldo:.2f}")
    elif opcion == "4":
        print("Gracias por usar el cajero.")
        break
    else:
        print("Opción no válida.")