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
            salir_bucle_principal = False
            while opcion != 6:
                # Leer recetas
                if opcion == 1:
                    letra = 'C'
                    while letra == 'C':
                        resultado = functions.read_recipes(nombre, ruta_recetas)
                        # Se evalúa el return de la función para comprobar si se debe ejecutar esta opción
                        if resultado["estado"] == "continuar":
                            print("\n")
                            letra = functions.eleccion_letra(nombre)

                        elif resultado["estado"] == "no válido":
                            functions.read_recipes(nombre, ruta_recetas)

                        elif resultado["estado"] == "volver inicio":
                            salir_bucle_principal = True
                            break

                    if salir_bucle_principal:
                        break

                    if letra == 'E':
                        break

                # Crear recetas
                if opcion == 2:
                    letra = 'C'
                    while letra == 'C':
                        resultado = functions.create_recipes(nombre, ruta_recetas)
                        # Se evalúa el return de la función para comprobar si se debe ejecutar esta opción
                        if resultado["estado"] == "continuar":
                            print("\n")
                            letra = functions.eleccion_letra(nombre)

                        elif resultado["estado"] == "no válido":
                            functions.create_recipes(nombre, ruta_recetas)

                        elif resultado["estado"] == "volver inicio":
                            salir_bucle_principal = True
                            break

                    if salir_bucle_principal:
                        break

                    if letra == 'E':
                        break

                # Crear categoría
                if opcion == 3:
                    letra = 'C'
                    while letra == 'C':
                        resultado = functions.create_category(nombre, ruta_recetas)
                        # Se evalúa el return de la función para comprobar si se debe ejecutar esta opción
                        if resultado["estado"] == "continuar":
                            print("\n")
                            letra = functions.eleccion_letra(nombre)

                        elif resultado["estado"] == "no válido":
                            functions.create_category(nombre, ruta_recetas)

                        elif resultado["estado"] == "volver inicio":
                            salir_bucle_principal = True
                            break

                    if salir_bucle_principal:
                        break

                    if letra == 'E':
                        break

                # Eliminar receta
                if opcion == 4:
                    letra = 'C'
                    while letra == 'C':
                        resultado = functions.remove_recipe(nombre, ruta_recetas)
                        # Se evalúa el return de la función para comprobar si se debe ejecutar esta opción
                        if resultado["estado"] == "continuar":
                            print("\n")
                            letra = functions.eleccion_letra(nombre)

                        elif resultado["estado"] == "no válido":
                            functions.remove_recipe(nombre, ruta_recetas)

                        elif resultado["estado"] == "volver inicio":
                            salir_bucle_principal = True
                            break

                    if salir_bucle_principal:
                        break

                    if letra == 'E':
                        break

                # Eliminar categoría
                if opcion == 5:
                    letra = 'C'
                    while letra == 'C':
                        resultado = functions.remove_category(nombre, ruta_recetas)
                        # Se evalúa el return de la función para comprobar si se debe ejecutar esta opción
                        if resultado["estado"] == "continuar":
                            print("\n")
                            letra = functions.eleccion_letra(nombre)

                        elif resultado["estado"] == "no válido":
                            functions.remove_category(nombre, ruta_recetas)

                        elif resultado["estado"] == "volver inicio":
                            salir_bucle_principal = True
                            break

                    if salir_bucle_principal:
                        break

                    if letra == 'E':
                        break

            if opcion == 6:
                print(F"{nombre}, has salido con éxito del menú")
                break

        elif opcion not in range(1, 7):
            print("La opción seleccionada no es válida\n")
            continue

    except ValueError:
        print("La opción introducida no es un número.\n")


