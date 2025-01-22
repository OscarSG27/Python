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
    categorias = {}
    clave_cat = 1
    directorio_categorias = Path(ruta_recetas)
    diccionario_completo = {}
    print("Deberás seleccionar una categoría: ")
    # For para mostrar las categorías disponibles de manera dinámica
    for categoria in directorio_categorias.iterdir():
        if categoria.is_dir():
            categorias[clave_cat] = categoria.name
            clave_cat += 1
    for clave, valor in categorias.items():
        print(clave, valor)

    # For para alimentar el diccionario completo
    for clave, nombre_categoria in categorias.items():
        # Construir la ruta completa de la categoría
        ruta_categoria = directorio_categorias / nombre_categoria

        # Crear el subdiccionario de recetas
        recetas = {
            receta_id + 1: receta.name  # Clave: número incremental, Valor: nombre del archivo
            for receta_id, receta in enumerate(ruta_categoria.iterdir())
            if receta.is_file()
        }

        # Añadir la categoría y su subdiccionario al diccionario completo
        diccionario_completo[clave] = recetas

    seleccion_categoria = int(input("Respuesta: "))

    if seleccion_categoria in diccionario_completo:
        recetas = diccionario_completo[seleccion_categoria]
        ruta = directorio_categorias / categorias[seleccion_categoria]
        print(f"{nombre}, has seleccionado la categoría: {categorias[seleccion_categoria]}. Estas son sus recetas: ")

        for clave, valor in recetas.items():
            print(f"{clave}: {valor}")

        # Selección de recetas

        seleccion_receta = int(input(f"{nombre}, introduce un número de receta para leerla: "))

        if seleccion_receta in recetas:
            print(f"A continuación se mostrará la receta de {recetas[seleccion_receta]}: ")
            archivo_seleccionado = recetas[seleccion_receta]
            ruta_archivo = ruta / archivo_seleccionado
            with open(ruta_archivo, 'r') as archivo:
                print(archivo.read())

    else:
        print("Valor introducido no válido.")


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
        archivo = input('Pon nombre al archivo: ')
        ruta_archivo = os.path.join(ruta_recetas, directorio, archivo)
        with open(ruta_archivo, 'w') as nueva_receta:
            nueva_receta.write(receta)

    # Ensaladas
    if categoria == 2:
        directorio = 'Ensaladas'
        receta = input(f"Introduce la receta a crear, {nombre}\n""Respuesta: " "\n")
        archivo = input('Pon nombre al archivo: ')
        ruta_archivo = os.path.join(ruta_recetas, directorio, archivo)
        with open(ruta_archivo, 'w') as nueva_receta:
            nueva_receta.write(receta)

    # Pastas
    if categoria == 3:
        directorio = 'Pastas'
        receta = input(f"Introduce la receta a crear, {nombre}\n""Respuesta: " "\n")
        archivo = input('Pon nombre al archivo: ')
        ruta_archivo = os.path.join(ruta_recetas, directorio, archivo)
        with open(ruta_archivo, 'w') as nueva_receta:
            nueva_receta.write(receta)
        print("Receta creada con éxito")

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



