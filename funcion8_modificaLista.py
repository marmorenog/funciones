#8. Función que recibe y modifica una lista:

def agregar_tarea(lista_tareas:list, tarea):# tiene dos parámetros, en una lista, se le agrega el list para que sea lista
    lista_tareas.append(tarea) #aqui se agrega la tarea
    print(f"Tarea {tarea} agregada.") #aqui coloca como se agrega la tarea

def mostrar_tareas(lista_tareas):
    if not lista_tareas:
           print("No hay tareas pendientes.")
           return #aqui sale del codigo
    print ("\nTareas pendientes:")
    for i, tarea in enumerate(lista_tareas,1): #la i es posición , tarea= un valor, el enumarate se cambia de valor y posición
        print(f"{i}.{tarea}") #aqui se imprime las tareas i posición y tarea

mis_tareas =[]
agregar_tarea(mis_tareas,"Estudiar Python") #aqui se guarda las tareas
agregar_tarea(mis_tareas, "Hacer ejercicio") #aqui se guarda en la lista
mostrar_tareas(mis_tareas) #aqui se se muestra ambas 