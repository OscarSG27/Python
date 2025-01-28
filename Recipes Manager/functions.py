import os
import shutil
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
    print("Pulsa V para volver al inicio")

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

    seleccion_categoria = input("Respuesta: ").upper()

    if seleccion_categoria.isnumeric():
        seleccion_categoria = int(seleccion_categoria)
        if seleccion_categoria in diccionario_completo:
            avanzar = False
            recetas = diccionario_completo[seleccion_categoria]
            ruta = directorio_categorias / categorias[seleccion_categoria]
            print(f"{nombre}, has seleccionado la categoría: {categorias[seleccion_categoria]}. "
                  f"Estas son sus recetas: ")

            while not avanzar:
                for clave, valor in recetas.items():
                    print(f"{clave}: {valor}")

                # Selección de recetas
                seleccion_receta = input(f"{nombre}, introduce un número de receta para leerla: ")

                if seleccion_receta.isnumeric():
                    seleccion_receta = int(seleccion_receta)
                    if seleccion_receta in recetas:
                        print(f"A continuación se mostrará la receta de {recetas[seleccion_receta]}: ")
                        archivo_seleccionado = recetas[seleccion_receta]
                        ruta_archivo = ruta / archivo_seleccionado
                        with open(ruta_archivo, 'r') as archivo:
                            print(archivo.read())
                        avanzar = True
                    else:
                        print("Código de receta no válido. Prueba de nuevo.")
                else:
                    print("Valor no válido, las recetas tienen códigos numéricos.")

            return {"error": False, "estado": "continuar"}

        else:
            print("Categoría no válida.")
            return {"error": True, "estado": "no válido"}

    # Opción de retorno al inicio por si entramos por error
    elif seleccion_categoria == "V":
        return {"error": False, "estado": "volver inicio"}

    # Manejo de cualquier otro caso no válido
    else:
        print("Valor introducido no válido.")
        return {"error": True, "estado": "no válido"}


def introducir_opcion(nombre):
    opcion = input(F"Elige una opción, {nombre}: \n""1.Leer recetas\n""2.Crear recetas\n""3.Crear categoría\n"
                   "4.Eliminar receta\n""5.Eliminar categoría\n""6.Finalizar programa\n""Opción: " "\n")
    return opcion


def eleccion_letra(nombre):
    letra = input(f"{nombre}, "
                  f"pulsa E para volver al menú principal o C para continuar una nueva consulta: ").upper()
    return letra


def create_recipes(nombre, ruta_recetas):
    categorias = {}
    clave_cat = 1
    directorio_categorias = Path(ruta_recetas)
    diccionario_completo = {}
    print("Selecciona la categoría: ")
    # For para mostrar las categorías disponibles de manera dinámica
    for categoria in directorio_categorias.iterdir():
        if categoria.is_dir():
            categorias[clave_cat] = categoria.name
            clave_cat += 1
    for clave, valor in categorias.items():
        print(clave, valor)

    print("Pulsa V para volver al inicio")
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

    seleccion_categoria = input("Respuesta: ").upper()

    if seleccion_categoria.isnumeric():
        seleccion_categoria = int(seleccion_categoria)
        if seleccion_categoria in diccionario_completo:
            print(f"{nombre}, has seleccionado la categoría: {categorias[seleccion_categoria]}. "
                  f"Vas a crear una receta en su interior ")
            print("Escribe la nueva receta: \n")
            nueva_receta = input()
            print("Pon nombre al archivo: \n")
            archivo = input() + '.txt'
            ruta = directorio_categorias / categorias[seleccion_categoria]
            ruta_receta = ruta / archivo
            with open(ruta_receta, 'w') as receta:
                receta.write(nueva_receta)
            print(f"Has creado el nuevo archivo: {archivo}")

            return {"error": False, "estado": "continuar"}
        else:
            print("Valor introducido no válido.")
            return {"error": True, "estado": "no válido"}
    elif seleccion_categoria == "V":
        return {"error": False, "estado": "volver inicio"}

    else:
        print("Valor introducido no válido.")
        return {"error": True, "estado": "no válido"}


def create_category(nombre, ruta_recetas):
    print(f"{nombre}, vas a crear una nueva categoría dentro de {ruta_recetas}")
    seleccion = input("Si te has equivocado, pulsa V para volver al inicio o C para continuar: ").upper()
    print("\n")

    if seleccion == "V":
        return {"error": False, "estado": "volver inicio"}
    elif seleccion == "C":

        while True:
            print("Introduce el nombre del directorio:")
            nuevo_directorio = input()
            ruta = Path(ruta_recetas) / nuevo_directorio

            # Comprobar si el directorio ya existe
            if ruta.exists():
                print(f"El directorio '{nuevo_directorio}' ya existe. Por favor, elige otro nombre.")
            else:
                # Crear el directorio si no existe
                ruta.mkdir()
                print(f"El directorio '{nuevo_directorio}' ha sido creado en la ruta '{ruta}'.")
                break  # Salir del bucle al crear el directorio correctamente
        return {"error": False, "estado": "continuar"}
    else:
        print("Valor introducido no válido")
        return {"error": True, "estado": "no válido"}


def remove_recipe(nombre, ruta_recetas):
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

    print("Pulsa V para volver al inicio")

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

    seleccion_categoria = input("Respuesta: ").upper()

    if seleccion_categoria.isnumeric():
        avanzar = False
        seleccion_categoria = int(seleccion_categoria)
        if seleccion_categoria in diccionario_completo:
            recetas = diccionario_completo[seleccion_categoria]
            ruta = directorio_categorias / categorias[seleccion_categoria]
            print(f"{nombre}, has seleccionado la categoría: {categorias[seleccion_categoria]}. "
                  f"Estas son sus recetas: ")

            while not avanzar:
                for clave, valor in recetas.items():
                    print(f"{clave}: {valor}")

                # Selección de recetas

                seleccion_receta = input(f"{nombre}, introduce un número de receta para eliminarla: ")

                if seleccion_receta.isnumeric():
                    seleccion_receta = int(seleccion_receta)
                    if seleccion_receta in recetas:
                        print(f"A continuación se eliminará la receta de {recetas[seleccion_receta]}: ")
                        archivo_seleccionado = recetas[seleccion_receta]
                        ruta_archivo = ruta / archivo_seleccionado
                        ruta_archivo.unlink()
                        print(f"La receta {archivo_seleccionado} ha sido eliminada")
                        avanzar = True
                    else:
                        print("Código de receta no válido. Prueba de nuevo.")
                else:
                    print("Deberás seleccionar un valor numérico")

        else:
            print("Valor introducido no válido.")
            return {"error": True, "estado": "no válido"}

        return {"error": False, "estado": "continuar"}

    elif seleccion_categoria == "V":
        return {"error": False, "estado": "volver inicio"}

    else:
        print("Valor introducido no válido.")
        return {"error": True, "estado": "no válido"}


def remove_category(nombre, ruta_recetas):
    categorias = {}
    clave_cat = 1
    directorio_categorias = Path(ruta_recetas)
    diccionario_completo = {}
    print("Deberás seleccionar la categoría que quieres eliminar: ")
    # For para mostrar las categorías disponibles de manera dinámica
    for categoria in directorio_categorias.iterdir():
        if categoria.is_dir():
            categorias[clave_cat] = categoria.name
            clave_cat += 1
    for clave, valor in categorias.items():
        print(clave, valor)
    print("Pulsa V para volver al inicio")

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

    seleccion_categoria = input("Respuesta: ").upper()

    if seleccion_categoria.isnumeric():
        seleccion_categoria = int(seleccion_categoria)
        if seleccion_categoria in diccionario_completo:
            ruta = directorio_categorias/categorias[seleccion_categoria]
            print(f"{nombre}, vas a eliminar la categoría: {categorias[seleccion_categoria]}.")
            shutil.rmtree(ruta)
            print("Categoría eliminada.")
            return {"error": False, "estado": "continuar"}
        else:
            print("Valor introducido no válido.")
            return {"error": True, "estado": "no válido"}

    elif seleccion_categoria == "V":
        return {"error": False, "estado": "volver inicio"}
    else:
        print("Valor introducido no válido.")
        return {"error": True, "estado": "no válido"}




