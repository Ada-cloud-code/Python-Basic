import math

def obtener_numero():
    while True:
        try:
            numero = float(input("Introduce un número: "))
            return numero
        except ValueError:
            print("Por favor, introduce un número válido.")

# Solicitar dos números
numero1 = obtener_numero()
numero2 = obtener_numero()

# Mostrar la multiplicación
multiplicacion = numero1 * numero2
print(f"La multiplicación de {numero1} y {numero2} es: {multiplicacion}")

# Evaluar cuál es mayor
if numero1 > numero2:
    print(f"El número mayor es: {numero1}")
elif numero1 < numero2:
    print(f"El número mayor es: {numero2}")
else:
    print("Ambos números son iguales.")

# Elegir un número para calcular su cuadrado y raíz
while True:
    opcion = input("Elige un número (1 o 2) para calcular su cuadrado y raíz: 1 para el primero, 2 para el segundo: ")
    if opcion == '1':
        elegido = numero1
        break
    elif opcion == '2':
        elegido = numero2
        break
    else:
        print("Opción inválida. Intenta de nuevo.")

# Calcular y mostrar cuadrado y raíz
cuadrado = elegido ** 2
raiz = math.sqrt(elegido)
print(f"El cuadrado de {elegido} es: {cuadrado}")
print(f"La raíz cuadrada de {elegido} es: {raiz}")
