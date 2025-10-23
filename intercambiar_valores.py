def intercambiar_valores():
    a = input("Ingrese A: ")
    b = input("Ingrese B: ")
    a, b = b, a
    print("Ahora A vale:", a)
    print("Ahora B vale:", b)