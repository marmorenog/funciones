#4. Parámetros con valor por defecto:

def crear_usuario(nombre,rol="estudiante"):
    print(f"Usuario: {nombre} | Rol: {rol}") #son string

crear_usuario("Maria ") #aqui se le da solamente un parámetro, valor por defecto
crear_usuario("Pedro", "administrador") #aqui dos parámetro, el valor por defecto se pisa y se cambia al administrador
crear_usuario("Laura",rol="docente") #aqui puede ser mas explicito, no es obligación, se puede escribir el nombre del parámetro y se pisa
