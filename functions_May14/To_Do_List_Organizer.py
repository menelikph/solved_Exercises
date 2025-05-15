todos = []  # Lista de tareas, cada tarea es un diccionario con nombre, prioridad y estado

def add_task(name, priority):
    # Verificar si la tarea ya existe
    for task in todos:
        if task["name"] == name:
            print(f"La tarea '{name}' ya existe.")
            return
    # Agregar nueva tarea con estado 'pending' (pendiente)
    todos.append({"name": name, "priority": priority, "status": "pending"})
    print(f"Tarea '{name}' agregada con prioridad '{priority}'.")

def complete_task(name):
    for task in todos:
        if task["name"] == name:
            task["status"] = "completed"
            print(f"Tarea '{name}' marcada como completada.")
            return
    print(f"No se encontró la tarea '{name}'.")

def filter_tasks(priority=None, status=None):
    result = todos  # Empezamos con toda la lista de tareas

    if priority is not None:
        filtered = []
        for task in result:
            if task["priority"] == priority:
                filtered.append(task)
        result = filtered

    if status is not None:
        filtered = []
        for task in result:
            if task["status"] == status:
                filtered.append(task)
        result = filtered
    return result

"""
def filter_tasks(priority=None, status=None):
    result = todos
    if priority is not None:
        result = [task for task in result if task["priority"] == priority]
    if status is not None:
        result = [task for task in result if task["status"] == status]
    return result
    """
