def area_perimetro_circulo():
    radio = float(input("Ingrese el radio: "))
    area = "math.pi" * (radio ** 2)
    perimetro = 2 * "math.pi" * radio
    print("Área:", area)
    print("Perímetro:", perimetro)