contador = 1
limite = 3

nombre = input("Ingresa tu nombre de usuario: ")

if nombre == "Geralber":
    
    contraseña = input("Ingresa tu contraseña: ")
    
    if contraseña == "1234":
        print("Ha podido ingresar a su cuenta.")
    
    elif not contraseña == "1234":
        
        while contador < limite:
            contador += 1
            contraseña = input("Incorrecto. Intentalo de nuevo: ")
            
            if contraseña == "1234":
                print("Ha podido ingresar a su cuenta.")
                break
            
            while contador == limite:
                print("Ha realizado 3 intentos maximo, vuelve a intentarlo mas tarde. ")
                break
            
    else:
        print("Fin. ")
    

else:
    print("Debe ingresar su nombre de usuario existente.")