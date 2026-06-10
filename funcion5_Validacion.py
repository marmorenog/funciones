# 5. Función de validación:

def es_mayor_de_edad(edad): #no tiene valor por defecto porque la lógica que se pregunta
    if edad >= 18: #si edad es mayor o igual a 18 
        return True #devuelve un positivo, no quiero que devuelva un mensaje 
    return False #devuelve un negativo

edad = int(input("Ingresa tu edad: ")) #aqui t
if es_mayor_de_edad(edad):
    print("Acceso permitido.")
else:
    print("Acceso Denegado")