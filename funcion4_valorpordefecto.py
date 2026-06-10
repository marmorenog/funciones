#4. Parámetros con valor por defecto:

def crear_usuario(nombre,rol="estudiante"):
    print(f"Usuario: {nombre} | Rol: {rol}")

crear_usuario("Maria")
crear_usuario("Pedro", "administrador")
crear_usuario("Laura",rol="docente")