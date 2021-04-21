# Crear un programa que lleve el control de notas en una base de datos (ARCHIVOS - usar json) HECHO
# Debe almacenar datos de estudiante (Nombre, carnet) - HECHO
# El programa debe alamcenar cualquier cantidad de notas para un estudiante - HECHO
# Debe calcular el promedio de cada estudiante HECHO
# Debe calcular los años de estudio a partir del carnet PENDIENTE
# Se debe poder mostrar la cantidad de estudiantes HECHO

# estudiante = {
#     'nombre': 'Luis Carlos',
#     'carnet': '1990-20-1302',
#     'notas': [70, 80, 90, 65, 61, 85, 70, 61, 65, 55, 50],
#     'promedio': 70.5
#     'annos_estudio': 1
# }

# lista_estudiantes = [estudiante1, estudiante2, ....]

# base_de_datos.json
import json
import string
import re

# lista_estudiantes = []

try:
    with open("base_de_datos.json", "r") as archivo_db:
        print("Leyendo base de datos...")
        lista_estudiantes = json.load(archivo_db)
        print("Base de datos cargada exitosamente")
except:
    print("Creando nueva base de datos...")
    lista_estudiantes = []


def calcular_promedio(lista_notas_estudiante):
    total_suma = 0
    # sumar todas las notas
    for nota in lista_notas_estudiante:
        total_suma = total_suma + nota
    # obtener cantidad de notas
    cantidad_notas = len(lista_notas_estudiante)
    # calcular promedio
    promedio = total_suma / cantidad_notas
    # retornar el promedio
    return promedio


def ingresar_nuevo_estudiante():
    # pedir datos de estudiante
    nombre = input("Ingrese nombre: ")
    carnet = ""
    while True:
        carnet = input("Ingrese carnet")
        if re.match('[0-9]{2}-[0-9]{4}$', carnet):
            estudiante_buscado = buscar_estudiante(carnet)
            if estudiante_buscado == 0:
                break
            else:
                print("El numero de carnet ya esta registrado")
        else:
            print("Carnet no valido")

    anno_ingreso = "20" + carnet.split('-')[0]
    while True:
        # agregar notas
        lista_notas = []
        opcion_notas = input("Desea ingresar una nota? (y / n): ")
        while opcion_notas == 'y' or opcion_notas == 'Y':
            nueva_nota = input("Ingrese la nota: ")
            # convertir en entero
            nueva_nota = int(nueva_nota)
            lista_notas.append(nueva_nota)
            opcion_notas = input("Desea ingresar otra nota? (y / n): ")
        if len(lista_notas) > 0:
            break
        else:
            print("Erro el usuario no se puede guardar con cero notas")
    # Ingreso de estudiante sin notas
    # while opcion_notas == 'N' or opcion_notas == 'n':
     #   lista_estudiantes.append(estudiante)

    # llamar al calculo de promedio
    promedio_estudiante = calcular_promedio(lista_notas)

    # cursos aprobados
    cursos_aprobados = [note for note in lista_notas if note >= 61]

    # porcentaje de cursos aprobados
    porcentaje_de_cursos_aprobados = len(
        cursos_aprobados) * 100 / len(lista_notas)

    # crear al nuevo estudiante
    estudiante = {
        'nombre': nombre,
        'carnet': carnet,
        'notas': lista_notas,
        'promedio': promedio_estudiante,
        'anno_de_ingreso': anno_ingreso,
    # cantidad de cursos asignados
        'cantidad_de_cursos_asignados': len(lista_notas),
        'cantidad_de_cursos_aprobados': len(cursos_aprobados),
        'porcentaje_de_cursos_aprobados': porcentaje_de_cursos_aprobados

    }
    # agregar el nuevo estudiante a la lista
    lista_estudiantes.append(estudiante)

    return


def buscar_estudiante(carnet_estudiante):
        busqueda = next(
    (estudiante for estudiante in lista_estudiantes if estudiante['carnet'] == carnet_estudiante), 0)
        if busqueda:
            return busqueda
        else:
            return False


def mostrar_lista_estudiantes():
    print('Listado de estudiantes \n')
    for estudiante in lista_estudiantes:
        print("------------------------------------------")
        print("------------------------------------------")
        print(f"nombre: {estudiante['nombre']}")
        print(f"carnet: {estudiante['carnet']}")
        print(f"notas: {estudiante['notas']}")
        print(f"promedio: {estudiante['promedio']}")
        print(f"anno_de_ingreso: {estudiante['anno_de_ingreso']}")
        print(f"cantidad_de_cursos_asignados: {estudiante['cantidad_de_cursos_asignados']}")
        print(f"cantidad_de_cursos_aprobados: {estudiante['cantidad_de_cursos_aprobados']}")
        print(f"porcentaje_de_cursos_aprobados: {estudiante['porcentaje_de_cursos_aprobados']}")
        print("------------------------------------------")
        print("------------------------------------------")


        
    return

def mostrar_cantidad_estudiantes():
    cantidad = len(lista_estudiantes)
    print(f'Hay {cantidad} estudiantes registrados')
    return

def buscar_alumno():
    print('Buscar un usuario')
    

def mostrar_menu():
    mensaje_menu = """Ingrese la opcion deseada\n
    1. Ingresar un nuevo estudiante\n
    2. Buscar un usuario\n
    3. Mostrar listado de usuarios\n
    4. Salir\n
    > 
    """
    opcion = input(mensaje_menu)
    opcion = int(opcion)
    if opcion == 1:
        # ingresar un nuevo estudiante
        ingresar_nuevo_estudiante()
    if opcion == 2:
        carnet = input("Ingrese el numero de carnte")
        estudiante_buscado = buscar_estudiante(carnet)
        if estudiante_buscado == 0:
            print("Estudiante no encontrado")
        else:
            print("Estudiante encontrado con exito")
            print("------------------------------------------")
            print("------------------------------------------")
            print(f"nombre: {estudiante_buscado['nombre']}")
            print(f"carnet: {estudiante_buscado['carnet']}")
            print(f"notas: {estudiante_buscado['notas']}")
            print(f"promedio: {estudiante_buscado['promedio']}")
            print(f"anno_de_ingreso: {estudiante_buscado['anno_de_ingreso']}")
            print(f"cantidad_de_cursos_asignados: {estudiante_buscado['cantidad_de_cursos_asignados']}")
            print(f"cantidad_de_cursos_aprobados: {estudiante_buscado['cantidad_de_cursos_aprobados']}")
            print(f"porcentaje_de_cursos_aprobados: {estudiante_buscado['porcentaje_de_cursos_aprobados']}")
            print("------------------------------------------")
            print("------------------------------------------")


    if opcion == 3:
        # mostrar cantidad de estudiante
        mostrar_cantidad_estudiantes()
        # mostrar lista estudiantes
        mostrar_lista_estudiantes()
    if opcion == 4:
        # salir
        print("Ingrese la opcion de salir que desee")
        opciones = input("a. Guardar y salir, b. Salir sin guardar")
        if opciones == "a" or opcion == "A":
            with open("base_de_datos.json", "w") as archivo_db:
                print("Guardando base de datos...")
                json.dump(lista_estudiantes, archivo_db)
        elif opciones == "b" or opciones == "B":
            print("Usted ha cerrado sin guardar los datos ingresados recientemente")
        return

    mostrar_menu()
    return

mostrar_menu()
