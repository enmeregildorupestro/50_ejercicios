texto = input("Ingrese una cadena: ").lower()
vocales = "aeiou"
contador = sum(1 for letra in texto if letra in vocales)
print(f"La cadena tiene {contador} vocal(es).")