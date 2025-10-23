palabra = input("Ingrese una palabra: ").lower()
if palabra == palabra[::-1]:
    print("La palabra es palíndroma.")
else:
    print("La palabra no es palíndroma.")