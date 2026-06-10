#6. Función de validación compuesta:
def validar_contrasena(contrasena):
    if len(contrasena) < 8: #
        return False, "Mínimo 8 caracteres" #aqui esta validando el largo de la contraseña y devuelve 2 cosas, si da false termina todo
    tiene_numero = False #se crep antes la variable
    for caracter in contrasena: #segundo for, ese ciclo for esta recorriedo letra por letra 
        if caracter.isdigit(): #encontrar un número
            tiene_numero = True #si tiene un número y da positivo 
    if not tiene_numero: #si no tiene número da otro
        return False, "Debe contener al menos un número" # si no tiene número da el false y termina la ejecución
    return True, "Contraseña válida" #acá sale y luego da verdadero y da el mensaje

clave = input("Crea tu contraseña: ")
valida, mensaje = validar_contrasena (clave) #aqui es son los dos parametros del validar contraseña
print(mensaje)