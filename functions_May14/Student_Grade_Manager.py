grades = {}

def add_student(name):
    if name in grades:
        print(f"Student '{name}' already exists.")
    else:
        grades[name] = []
        print(f"Student '{name}' added to the system.")

def add_grade(name, grade):
    if name not in grades:
        print(f"Student '{name}' not found.")
    else:
        grades[name].append(grade)
        print(f"Grade {grade} added to student '{name}'.")

def get_average(name):
    if name not in grades:
        return None
    if len(grades[name]) == 0:
        return 0
    promedio = sum(grades[name]) / len(grades[name])
    return promedio
