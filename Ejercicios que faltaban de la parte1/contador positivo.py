contador = 0

numero = float(input("Ingresa un número negativo para salir: "))

while numero >= 0:
    contador = contador + 1

    numero = float(input("Ingresa otro número: "))

print(f"Ingresaste {contador} números positivos.")
