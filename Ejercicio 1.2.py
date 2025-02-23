def mostrar_pares_o_impares(opcion):
    numeros = []
    if opcion == "par":
        for i in range(2, 1001, 2):
            numeros.append(i)
    elif opcion == "impar":
        for i in range(1, 1001, 2):
            numeros.append(i)
    
    suma = sum(numeros)
    promedio = suma / len(numeros) if len(numeros) > 0 else 0
    print(f"Números {opcion}s entre 1 y 1000: {numeros}")
    print(f"Suma: {suma}")
    print(f"Promedio: {promedio}")

# Elegir opción
while True:
    opcion = input("Elige una opción (par/impar): ").lower()
    if opcion in ["par", "impar"]:
        mostrar_pares_o_impares(opcion)
        break
    else:
        print("Opción inválida. Elige 'par' o 'impar'.")
