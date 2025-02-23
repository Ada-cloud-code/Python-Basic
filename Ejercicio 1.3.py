def contar_divisores(num):
    divisores = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisores.append(i)
    return divisores

# Solicitar un número positivo
while True:
    try:
        numero = int(input("Introduce un número entero positivo: "))
        if numero <= 0:
            print("Por favor, introduce un número positivo.")
        else:
            divisores = contar_divisores(numero)
            print(f"Los divisores de {numero} son: {divisores}")
            print(f"Cantidad de divisores: {len(divisores)}")
            break
    except ValueError:
        print("Por favor, introduce un número válido.")
