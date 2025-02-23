def mostrar_vocales(palabra):
    vocales = "aeiouAEIOU"
    solo_vocales = [letra for letra in palabra if letra in vocales]
    consonantes = [letra for letra in palabra if letra not in vocales]
    print(f"Vocales: {''.join(solo_vocales)}")
    print(f"Total de letras: {len(palabra)}")
    print(f"Total de vocales: {len(solo_vocales)}")
    print(f"Total de consonantes: {len(consonantes)}")

def deletrear_inverso(palabra):
    print(f"Palabra en orden inverso: {palabra[::-1]}")

def primera_y_ultima(palabra):
    print(f"Primera letra: {palabra[0]}")
    print(f"Última letra: {palabra[-1]}")

# Solicitar una palabra
palabra = input("Introduce una palabra: ")

# Elegir opción
while True:
    opcion = input("Elige una opción (1, 2, 3):\n1. Vocales y conteo\n2. Deletreo inverso\n3. Primera y última letra\n")
    if opcion == "1":
        mostrar_vocales(palabra)
        break
    elif opcion == "2":
        deletrear_inverso(palabra)
        break
    elif opcion == "3":
        primera_y_ultima(palabra)
        break
    else:
        print("Opción inválida. Intenta de nuevo.")
