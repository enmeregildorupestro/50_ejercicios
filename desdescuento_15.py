def descuento_15():
    precio = float(input("Valor de la compra: "))
    descuento = precio * 0.15
    total = precio - descuento
    print("Descuento:", descuento)
    print("Total a pagar:", total)