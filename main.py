import functions

# Llamamos a la función que nos permite obtener el nombre del usuario
nombre = functions.obtener_nombre().capitalize()
print(f"Bienvenido al administrador de recetas, {nombre}\n")

# Llamamos a la función que nos permite obtener la ruta
ruta_recetas = functions.obtener_ruta()
print(F"{nombre}, la ruta de la carpeta recetas es: {ruta_recetas}\n")

# Llamamos a la función que nos permite obtener el número total de archivos
carpeta = functions.obtener_ruta()
total_archivos = functions.contar_archivos(carpeta)
print(F"El número total de recetas es de: {total_archivos}\n")

# Elegimos la opción del menú que queramos y vamos llamando a las funciones que contienen la lógica
while True:
    try:
        opcion = int(functions.introducir_opcion(nombre))
        if opcion in range(1, 7):
            while opcion != 6:
                # Leer recetas
                if opcion == 1:

                    letra = 'C'
                    while letra == 'C':
                        vuelta_inicio = functions.read_recipes(nombre, ruta_recetas)
                        error = functions.read_recipes(nombre, ruta_recetas)
                        # Se evalúa el return de la función para comprobar si se debe ejecutar esta opción
                        if not vuelta_inicio and not error:
                            print("\n")
                            letra = functions.eleccion_letra(nombre)
                        elif not vuelta_inicio and error:
                            functions.read_recipes(nombre, ruta_recetas)
                        else:
                            opcion = int(functions.introducir_opcion(nombre))
                            break

                    if letra == 'E':
                        opcion = int(functions.introducir_opcion(nombre))

                # Crear recetas
                if opcion == 2:
                    letra = 'C'
                    while letra == 'C':
                        vuelve_inicio = functions.create_recipes(nombre, ruta_recetas)
                        if not vuelve_inicio:
                            print("\n")
                            letra = functions.eleccion_letra(nombre)
                        else:
                            opcion = int(functions.introducir_opcion(nombre))
                            break

                    if letra == 'E':
                        opcion = int(functions.introducir_opcion(nombre))

                # Crear categoría
                if opcion == 3:
                    letra = 'C'
                    while letra == 'C':
                        vuelve_inicio = functions.create_category(nombre, ruta_recetas)
                        if not vuelve_inicio:
                            print("\n")
                            letra = functions.eleccion_letra(nombre)
                        else:
                            opcion = int(functions.introducir_opcion(nombre))
                            break

                    if letra == 'E':
                        opcion = int(functions.introducir_opcion(nombre))

                # Eliminar receta
                if opcion == 4:
                    letra = 'C'
                    while letra == 'C':
                        vuelve_inicio = functions.remove_recipe(nombre, ruta_recetas)
                        if not vuelve_inicio:
                            print("\n")
                            letra = functions.eleccion_letra(nombre)
                        else:
                            opcion = int(functions.introducir_opcion(nombre))
                            break

                    if letra == 'E':
                        opcion = int(functions.introducir_opcion(nombre))

                # Eliminar categoría
                if opcion == 5:
                    letra = 'C'
                    while letra == 'C':
                        vuelve_inicio = functions.remove_category(nombre, ruta_recetas)
                        if not vuelve_inicio:
                            print("\n")
                            letra = functions.eleccion_letra(nombre)
                        else:
                            opcion = int(functions.introducir_opcion(nombre))
                            break

                    if letra == 'E':
                        opcion = int(functions.introducir_opcion(nombre))

            if opcion == 6:
                print(F"{nombre}, has salido con éxito del menú")
                break

        elif opcion not in range(1, 7):
            print("La opción seleccionada no es válida\n")

    except ValueError:
        print("La opción introducida no es un número.\n")


