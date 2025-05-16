from datetime import time

# Diccionario con vuelos
vuelos = {
    "AV101": {
        "origen": "Lima",
        "destino": "Bogotá",
        "asientos": ["A1", "A2", "A3"],
        "horario": [15, 30]
    },
    "LA202": {
        "origen": "Santiago",
        "destino": "Quito",
        "asientos": ["B1", "B2", "B3"],
        "horario": [10, 45]
    }
}

# Total de asientos por vuelo
asientos_totales = {
    "AV101": 3,
    "LA202": 3
}

# Validar código del vuelo (dos letras + tres números)
def validar_codigo_vuelo(codigo):
    if len(codigo) != 5: #Esta línea verifica si la longitud del código de vuelo es exactamente 5 caracteres.
        return False #Si la longitud no es 5, la función retorna False
    letras = codigo[:2]
    numeros = codigo[2:]
    return letras.isalpha() and letras.isupper() and numeros.isdigit() 
"""
letras.isalpha(): Verifica si los primeros 2 caracteres son letras (alfabéticas).
letras.isupper(): Verifica si los primeros 2 caracteres son letras mayúsculas.
numeros.isdigit(): Verifica si los últimos 3 caracteres son dígitos (numéricos).
La función retorna True solo si todas estas condiciones se cumplen. Si alguna de las condiciones falla, la función retorna False.
"""

# Validar asiento (una letra + un número)
def validar_asiento(asiento):
    if len(asiento) < 2: #len() se utiliza para obtener la longitud de un objeto. Puede ser aplicada a varios tipos de objetos, como cadenas de texto, listas, tuplas, diccionarios, conjuntos, y otros iterables. 
        return False
    letra = asiento[0]
    numero = asiento[1:]
    return letra.isalpha() and letra.isupper() and numero.isdigit()

# Validar horario con datetime
def validar_horario(hora, minuto):
    try:
        _ = time(hora, minuto) 
        """
        El underscore ( _ )es una convención en Python que se utiliza para 
        denotar una variable que no se va a utilizar después. En este caso, no nos interesa el o
        bjeto time creado, solo queremos verificar si se puede crear sin lanzar una excepción.
        """
        return True
    except:
        return False

# Mostrar vuelos
def mostrar_vuelos():
    print("\n--- VUELOS DISPONIBLES ---")
    for codigo, datos in vuelos.items():
        h, m = datos["horario"]
        print(f"{codigo}: {datos['origen']} -> {datos['destino']} a las {h}:{m:02}")
        print("Asientos disponibles:", datos["asientos"])
        print()

# Reservar asiento
def reservar_asiento():
    codigo = input("Código del vuelo (ej: AV101): ").upper() #upper convertir a mayusculas
    if not validar_codigo_vuelo(codigo):
        print("Formato inválido. Usa dos letras y tres números (ej: AV101).")
        return
    if codigo not in vuelos:
        print("Vuelo no encontrado.")
        return

    asiento = input("Asiento a reservar (ej: A1): ").upper()
    if not validar_asiento(asiento):
        print("Formato de asiento inválido.")
        return

    if asiento not in vuelos[codigo]["asientos"]:
        print("Ese asiento ya está ocupado o no existe.")
        return

    vuelos[codigo]["asientos"].remove(asiento)
    print(f"Asiento {asiento} reservado en el vuelo {codigo}.")

# Calcular ocupación
def calcular_ocupacion():
    codigo = input("Código del vuelo: ").upper()
    if codigo not in vuelos:
        print("Vuelo no encontrado.")
        return

    total = asientos_totales[codigo]
    libres = len(vuelos[codigo]["asientos"])
    ocupados = total - libres
    porcentaje = (ocupados / total) * 100
    print(f"Vuelo {codigo}: {ocupados} asientos ocupados ({round(porcentaje, 2)}%).")

# Generar archivo de reporte
def generar_reporte():
    vuelos_ordenados = sorted(vuelos.items(), key=lambda v: time(v[1]["horario"][0], v[1]["horario"][1]))
    with open("reporte_vuelos.txt", "w") as archivo:
        for codigo, datos in vuelos_ordenados:
            h, m = datos["horario"]
            linea = f"{codigo}: {datos['origen']} -> {datos['destino']} a las {h}:{m:02}\n"
            archivo.write(linea)
    print("Reporte generado en 'reporte_vuelos.txt'.")

# Menú del programa
def menu():
    while True:
        print("\n1. Ver vuelos")
        print("2. Reservar asiento")
        print("3. Calcular ocupación")
        print("4. Generar reporte")
        print("5. Salir")
        opcion = input("Opción: ")

        if opcion == "1":
            mostrar_vuelos()
        elif opcion == "2":
            reservar_asiento()
        elif opcion == "3":
            calcular_ocupacion()
        elif opcion == "4":
            generar_reporte()
        elif opcion == "5":
            print("¡Hasta pronto!")
            break
        else:
            print("Opción inválida.")

# Ejecutar el programa
menu()