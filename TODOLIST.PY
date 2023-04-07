# Crea una lista vacía para almacenar las tareas
tareas = []

# Función para agregar una tarea a la lista
def agregar_tarea():
    tarea = input("Ingresa una nueva tarea: ")
    tareas.append({"tarea": tarea, "completado": False})
    print("Tarea agregada.")

# Función para mostrar la lista de tareas
def mostrar_tareas():
    print("Lista de tareas:")
    for i, tarea in enumerate(tareas):
        estado = "completado" if tarea["completado"] else "pendiente"
        print(f"{i+1}. {tarea['tarea']} ({estado})")

# Función para marcar una tarea como completada
def completar_tarea():
    mostrar_tareas()
    indice = int(input("Ingresa el número de la tarea que completaste: ")) - 1
    tareas[indice]["completado"] = True
    print("Tarea completada.")

# Menú principal
while True:
    print("\nSelecciona una opción:")
    print("1. Agregar tarea")
    print("2. Mostrar tareas")
    print("3. Completar tarea")
    print("4. Salir")
    opcion = input("> ")

    if opcion == "1":
        agregar_tarea()
    elif opcion == "2":
        mostrar_tareas()
    elif opcion == "3":
        completar_tarea()
    elif opcion == "4":
        break
    else:
        print("Opción inválida.")
