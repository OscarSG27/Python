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
opcion = int(functions.introducir_opcion(nombre))
while opcion != 6:
    # Leer recetas
    if opcion == 1:
        letra = 'C'
        while letra == 'C':
            functions.opcion_salir_continuar_read_recipes(nombre, ruta_recetas)
            letra = functions.eleccion_letra(nombre)

        if letra == 'E':
            opcion = int(functions.introducir_opcion(nombre))

    # Crear recetas
    if opcion == 2:
        letra = 'C'
        while letra == 'C':
            functions.opcion_salir_continuar_create_recipes(nombre, ruta_recetas)  # cambiar por la funcion de creacion
            letra = functions.eleccion_letra(nombre)

        if letra == 'E':
            opcion = int(functions.introducir_opcion(nombre))





if opcion == 6:
    print(F"{nombre}, has salido con éxito del menú")
