import os
from pathlib import Path


def obtener_nombre():
    nombre = input("Por favor, escribe tu nombre: ")
    return nombre


def obtener_ruta():
    directorio_raiz = os.path.abspath(os.sep)

    ruta_recetas = os.path.join(directorio_raiz, 'Recetas')
    return ruta_recetas


def contar_archivos(carpeta):
    path = Path(carpeta)
    contador = sum(1 for _ in path.rglob('*.txt'))
    return contador


def leer_recetas(ruta):
    with open(ruta, "r") as archivo:
        contenido = archivo.read()
        return contenido


def read_recipes(nombre, ruta_recetas):
    categoria = int(input("Deberás elegir una categoría:\n"
                          "1.Carnes\n"
                          "2.Ensaladas\n"
                          "3.Pastas\n"
                          "4.Postres\n"
                          "Categoría: ""\n"))

    # Carnes
    if categoria == 1:
        directorio = Path(ruta_recetas, 'Carnes')
        recetas = {}
        clave = 1
        print(f"¿Qué receta quieres leer, {nombre}?")
        for archivo in directorio.iterdir():
            if archivo.is_file():
                recetas[clave] = archivo.name
                clave += 1

        for clave, valor in recetas.items():
            print(clave, valor)

        try:
            receta = int(input("Respuesta: "))
            if receta not in recetas:
                print("Clave no válida")
            else:
                print(f"Receta seleccionada: {recetas[receta]}")
                archivo_seleccionado = recetas[receta]
                ruta_archivo = directorio / archivo_seleccionado
                with open(ruta_archivo, 'r') as archivo:
                    print(archivo.read())

        except ValueError:
            print("Por favor, ingresa un número válido.")

    # Ensaladas
    if categoria == 2:
        directorio = Path(ruta_recetas, 'Ensaladas')
        recetas = {}
        clave = 1
        print(f"¿Qué receta quieres leer, {nombre}?")
        for archivo in directorio.iterdir():
            if archivo.is_file():
                recetas[clave] = archivo.name
                clave += 1

        for clave, valor in recetas.items():
            print(clave, valor)

        try:
            receta = int(input("Respuesta: "))
            if receta not in recetas:
                print("Clave no válida")
            else:
                print(f"Receta seleccionada: {recetas[receta]}")
                archivo_seleccionado = recetas[receta]
                ruta_archivo = directorio / archivo_seleccionado
                with open(ruta_archivo, 'r') as archivo:
                    print(archivo.read())

        except ValueError:
            print("Por favor, ingresa un número válido.")

    # Pastas
    if categoria == 3:
        directorio = Path(ruta_recetas, 'Pastas')
        recetas = {}
        clave = 1
        print(f"¿Qué receta quieres leer, {nombre}?")
        for archivo in directorio.iterdir():
            if archivo.is_file():
                recetas[clave] = archivo.name
                clave += 1

        for clave, valor in recetas.items():
            print(clave, valor)

        try:
            receta = int(input("Respuesta: "))
            if receta not in recetas:
                print("Clave no válida")
            else:
                print(f"Receta seleccionada: {recetas[receta]}")
                archivo_seleccionado = recetas[receta]
                ruta_archivo = directorio / archivo_seleccionado
                with open(ruta_archivo, 'r') as archivo:
                    print(archivo.read())

        except ValueError:
            print("Por favor, ingresa un número válido.")

    # Postres
    if categoria == 4:
        directorio = Path(ruta_recetas, 'Postres')
        recetas = {}
        clave = 1
        print(f"¿Qué receta quieres leer, {nombre}?")
        for archivo in directorio.iterdir():
            if archivo.is_file():
                recetas[clave] = archivo.name
                clave += 1

        for clave, valor in recetas.items():
            print(clave, valor)

        try:
            receta = int(input("Respuesta: "))
            if receta not in recetas:
                print("Clave no válida")
            else:
                print(f"Receta seleccionada: {recetas[receta]}")
                archivo_seleccionado = recetas[receta]
                ruta_archivo = directorio / archivo_seleccionado
                with open(ruta_archivo, 'r') as archivo:
                    print(archivo.read())

        except ValueError:
            print("Por favor, ingresa un número válido.")


def introducir_opcion(nombre):
    opcion = input(F"Elige una opción, {nombre}: \n""1.Leer recetas\n""2.Crear recetas\n""3.Crear categoría\n"
                   "4.Eliminar receta\n""5.Eliminar categoría\n""6.Finalizar programa\n""Opción: " "\n")
    return opcion


def eleccion_letra(nombre):
    letra = input(f"{nombre}, "
                  f"pulsa E para volver al menú principal o C para continuar una nueva consulta: ").upper()
    return letra


def opcion_salir_continuar_read_recipes(nombre, ruta_recetas):
    read_recipes(nombre, ruta_recetas)
    print('\n')


def create_recipes(nombre, ruta_recetas):
    categoria = int(input("Deberás elegir una categoría:\n"
                          "1.Carnes\n"
                          "2.Ensaladas\n"
                          "3.Pastas\n"
                          "4.Postres\n"
                          "Categoría: ""\n"))

    # Carnes
    if categoria == 1:
        directorio = 'Carnes'
        receta = input(f"Introduce la receta a crear, {nombre}\n""Respuesta: " "\n")
        archivo = input('Pon nombre al archivo')
        ruta_archivo = os.path.join(ruta_recetas, directorio, archivo)
        with open(ruta_archivo, 'w') as nueva_receta:
            nueva_receta.write(receta)

    # Ensaladas
    if categoria == 2:
        directorio = 'Ensaladas'
        receta = input(f"Introduce la receta a crear, {nombre}\n""Respuesta: " "\n")
        archivo = input('Pon nombre al archivo')
        ruta_archivo = os.path.join(ruta_recetas, directorio, archivo)
        with open(ruta_archivo, 'w') as nueva_receta:
            nueva_receta.write(receta)

    # Pastas
    if categoria == 3:
        directorio = 'Pastas'
        receta = input(f"Introduce la receta a crear, {nombre}\n""Respuesta: " "\n")
        archivo = input('Pon nombre al archivo')
        ruta_archivo = os.path.join(ruta_recetas, directorio, archivo)
        with open(ruta_archivo, 'w') as nueva_receta:
            nueva_receta.write(receta)

    # Postres
    if categoria == 4:
        directorio = 'Postres'
        receta = input(f"Introduce la receta a crear, {nombre}\n""Respuesta: " "\n")
        archivo = input('Pon nombre al archivo: ')
        ruta_archivo = os.path.join(ruta_recetas, directorio, archivo)
        with open(ruta_archivo, 'w') as nueva_receta:
            nueva_receta.write(receta)


def opcion_salir_continuar_create_recipes(nombre, ruta_recetas):
    create_recipes(nombre, ruta_recetas)
    print('\n')



