import cv2
import face_recognition as fr
import os
import numpy as np
from datetime import datetime

# Crear bbdd

ruta = "Empleados"
imagenes = []
nombres_empleados = []
lista_empleados = os.listdir(ruta)

for nombre in lista_empleados:
    imagen_actual = cv2.imread(f'{ruta}/{nombre}')
    imagenes.append(imagen_actual)
    nombres_empleados.append(os.path.splitext(nombre)[0])

print(nombres_empleados)


# Codificar imágenes
def codificar(imagenes):
    # Crer lista de imagenes codificadas
    lista_codificada = []

    # Pasar todas las imágenes a RGB
    for imagen in imagenes:
        imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)

        # CODIFICAR
        codificado = fr.face_encodings(imagen)[0]

        # agregar a la lista
        lista_codificada.append(codificado)

    return lista_codificada


# Registrar las asistencias

def registrar_asistencia(persona):
    f = open('registros.csv', 'r+')
    lista_datos = f.readlines()
    nombres_registro = []
    for linea in lista_datos:
        ingreso = linea.split(',')
        nombres_registro.append(ingreso[0])

    if persona not in nombres_registro:
        ahora = datetime.now()
        string_ahora = ahora.strftime('%H:%M:%S')
        f.writelines(f"\n{persona}, {string_ahora}")


lista_empleados_codificada = codificar(imagenes)

# Imagen de cámara web
captura = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# Leer imagen de la cámara
exito, imagen = captura.read()

if not exito:
    print("Error al tomar la foto")
else:
    # Reconocer cara
    cara_captura = fr.face_locations(imagen)

    # Codificar la cara capturada
    cara_captura_codificada = fr.face_encodings(imagen, cara_captura)

    # Buscar coincidencias entre imagen y lista de fotos
    for caracodif, caraubic in zip(cara_captura_codificada, cara_captura):
        coincidencias = fr.compare_faces(lista_empleados_codificada, caracodif)
        distancias = fr.face_distance(lista_empleados_codificada, caracodif)

        print(distancias)

        indice_coincidencia = np.argmin(distancias)

        # Mostrar coincidencias si las hay
        if distancias[indice_coincidencia] > 0.6:
            print("No se han encontrado coincidencias")
        else:
            # Buscar el nombre del empleado encontrado
            nombre = nombres_empleados[indice_coincidencia]

            y1, x2, y2, x1 = caraubic
            cv2.rectangle(imagen, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(imagen, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(imagen, nombre, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1)
            registrar_asistencia(nombre)

            # Mostrar la imagen obtenida
            cv2.imshow("Imagen web empleado", imagen)

            # mantener ventana abierta
            cv2.waitKey(0)
