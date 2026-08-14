tareas = []

def mostrar_menu():
    print("\nGESTOR DE TAREAS")
    print("1. Agregar tarea")
    print("2. Listar tareas")
    print("3. Mostrar progreso")
    print("4. Salir")

def agregar_tarea():
    nombre = input("Tarea: ")
    tarea = {
        "nombre": nombre,
        "completada": False
    }
    tareas.append(tarea)
    
def listar_tareas():
    for tarea in tareas:
        print(
            tarea["nombre"],
            tarea["completada"]
        )
        
def mostrar_progreso():
    total = len(tareas)
    if total == 0:
        print("Sin tareas")
        return
    completadas = 0
    for tarea in tareas:
        if tarea["completada"]:
            completadas += 1
    porcentaje = (
        completadas * 100 / total
    )
feature/agregar-tarea

print("GESTOR DE TAREAS DEL EQUIPO")
while True:
    mostrar_menu()
    opcion = input("Opcion: ")

    if opcion == "1":
        agregar_tarea()
    elif opcion == "2":
        listar_tareas()
    elif opcion == "3":
        mostrar_progreso()
    elif opcion == "4":
        break
    else:
        print("Opción no válida")
    
main
