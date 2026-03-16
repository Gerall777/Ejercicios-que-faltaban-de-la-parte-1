saldo = 100
permiso_retiro = 10

usuario = input("Ingrese su nombre de usuario: ")
pin = int(input("Por favor, ingrese su numero de pin: "))

if pin == 1234:
    print("Puede Continuar. ")
    while saldo >= permiso_retiro:
        print(f"Saldo disponible: {saldo:.2f}")

        retiro = float(input("¿Cuanto desea retirar?: "))

        saldo = saldo - retiro

        if retiro > permiso_retiro and retiro < saldo:
            print(
                f"estimado {usuario}, a retirado: {retiro:.2f} y le queda {saldo:.2f} de saldo"
            )
            print(f"Le queda {saldo:.2f} de saldo")
        else:
            print("Lo siento, no tiene esa cantidad suficiente para retirar. ")

    while not saldo >= permiso_retiro:
        print(
            "Vuelve a retirar cuando tengas mas de 10 de saldo. \nQue tenga un excelente dia."
        )
        break


else:
    print("No pudo ingresar al banco. ")
