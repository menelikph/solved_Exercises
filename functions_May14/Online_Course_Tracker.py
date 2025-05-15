courses = []  # Lista para guardar cursos, cada curso es una lista [nombre, horas, inscritos]

def add_course(name, hours, enrolled):
    for course in courses:
        if course[0] == name:
            print(f"El curso '{name}' ya existe.")
            return
    courses.append([name, hours, enrolled])
    print(f"Curso '{name}' agregado con {hours} horas y {enrolled} inscritos.")

def update_enrollment(name, new_enrolled):
    for course in courses:
        if course[0] == name:
            course[2] = new_enrolled
            print(f"Inscritos en el curso '{name}' actualizados a {new_enrolled}.")
            return
    print(f"El curso '{name}' no existe.")

def filter_by_hours(min_hours):
    result = []
    for course in courses:
        if course[1] >= min_hours:
            result.append(course[0])
    return result
