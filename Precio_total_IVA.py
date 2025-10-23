precio = float(input("Ingrese el precio del producto: "))
iva = float(input("Ingrese el porcentaje de IVA (por ejemplo 19 para 19%): "))
total = precio + (precio * iva / 100)
print("El precio total con IVA es:", total)