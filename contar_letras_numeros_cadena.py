cadena = input("Ingrese una cadena: ")
letras = sum(c.isalpha() for c in cadena)
digitos = sum(c.isdigit() for c in cadena)
print(f"Letras: {letras}, Dígitos: {digitos}")