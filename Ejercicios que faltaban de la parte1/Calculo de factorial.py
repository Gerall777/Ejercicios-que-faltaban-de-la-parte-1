# Calculo de factorial

numero = int(input("Ingresar un numero: "))

factorial = 1


for n in range(1, (numero + 1)):
    factorial = factorial * n

print(f"El factorial de {numero} es: {factorial}.")
