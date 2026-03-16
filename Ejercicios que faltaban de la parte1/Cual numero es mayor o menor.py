print("Veamos cual de los tres numeros es mayor o menor\n")

numero1 = int(input("Introduce el primero numero: "))
numero2 = int(input("Introduce el segundo numero: "))
numero3 = int(input("Introduce el tercer numero: "))

if numero1 > numero2 and numero1 > numero3:
    print(f"{numero1} es mayor que {numero2} y {numero3}. ")
elif numero1 > numero2 and numero1 < numero3:
    print(f"{numero1} es mayor que {numero2} y menor que {numero3}")

elif numero2 > numero1 and numero2 > numero3:
    print(f"{numero2} es mayor que {numero1} y {numero3}. ")
elif numero2 > numero1 and numero2 < numero3:
    print(f"{numero2} es mayor que {numero1} y menor que {numero3}. ")

elif numero3 > numero1 and numero3 > numero2:
    print(f"{numero3} es mayor que {numero1} y {numero2}")

elif numero3 > numero1 and numero3 < numero2:
    print(f"{numero3} es mayor que {numero1} y menor que {numero2}")

else:
    print("Fin de la ejecucion.")
