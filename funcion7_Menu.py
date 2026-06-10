# 7. Función para menú:

def mostrar_menu():
    print("\n=== MENÚ PRINCIPAL===")
    print("1.Ver productos")
    print("2.Agregar productos")
    print("3.Salir")

def ver_productos():
    print("Lista de productos: [vacía]") #simulando la lista por eso es vacía 

def agregar_productos():
    nombre = input ("Nombre del producto: ")
    print (f"{nombre} agregado correctamente")

def ejecutar_menu():
    while True:
        mostrar_menu() #esta invocando la funcion
        opcion = input("Elige una opción: ") #escoger una opción
        if opcion=="1": #se escoge la función
            ver_productos() # se invoca a la función ver productos
        elif opcion=="2":
            agregar_productos() #aqui a la función agregar productos
        elif opcion=="3":
            print("Hasta pronto") #termina el ciclo
            break #termina la función
        else:
            print("Opción incorrecta") #cae en el ciclo

ejecutar_menu() #aqui se invoca la función de ejecuctar menu 