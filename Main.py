tareas = []

def mostrar_menu():
  print("Gestor de tareas")
  print("1. Agregar tarea")
  print("2. Listar tareas")
  print("3. Mostrar progreso")
  print("4. Salir")










def listar_tareas():
    for tarea in tareas:
        print(
            tarea["nombre"],
            tarea["completada"]
        )