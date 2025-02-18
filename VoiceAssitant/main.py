import pyttsx3
import speech_recognition as sr
import pywhatkit
import pyjokes
import webbrowser
import datetime
import wikipedia


# Escuchar micrófono y devolver el audio como texto
def transformar_audio_texto():
    # Almacenar el Recognizer en una variable
    r = sr.Recognizer()

    # Configurar el micro
    with sr.Microphone() as origen:
        r.adjust_for_ambient_noise(origen, duration=1)  # Ajusta al ruido de fondo
        print("Ya puedes hablar")  # Este mensaje se mostrará antes

        r.pause_threshold = 1.2  # Tiempo de pausa antes de parar la grabación
        r.non_speaking_duration = 0.6  # Tiempo de silencio antes de empezar a grabar

        audio = r.listen(origen)  # Empieza a escuchar inmediatamente

        try:
            # convertir el audio en texto usando la API de reconocimiento de voz de Google.
            pedido = r.recognize_google(audio, language="es-ES")

            # prueba de que transformo la voz en texto
            print("Has dicho: " + pedido)

            # Return pedido
            return pedido

        except sr.UnknownValueError:
            # Prueba de que no funciona
            print("No ha funcionado")

            return "No te entendí"

            # Si no puede traducir
        except sr.RequestError:
            print("No hay servicio")
            return "No entendí"

        except:
            print("Algo no ha salido bien")
            return "No te entendí"


# Función de voz del asistente
def hablar(mensaje):
    # Opciones de vor/idioma
    id1 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-ES_HELENA_11.0'
    id2 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'

    # Encender el motor de pyttsx3
    engine = pyttsx3.init()
    engine.setProperty('voice', id1)

    # Pronunciar mensaje
    engine.say(mensaje)
    engine.runAndWait()


# Función para que nos diga el día
def pedir_dia():
    dia = datetime.date.today()
    print(dia)

    # Crear una variable para el día de la semana
    dia_semana = dia.weekday()
    print(dia_semana)

    # Diccionario con días de la semana
    calendario = {0: 'Lunes',
                  1: 'Martes',
                  2: 'Miércoles',
                  3: 'Jueves',
                  4: 'Viernes',
                  5: 'Sábado',
                  6: 'Domingo'}
    # Decir el día de la semana
    hablar(f'Hoy es {calendario[dia_semana]}, {dia}.')


# Función para que nos diga la hora
def pedir_hora():
    hora = datetime.datetime.now()
    hora = f'Son las {hora.hour} horas {hora.minute} minutos'
    hablar(hora)



# Saludar

def saludo_inicial():
    hablar("Por favor, dime tu nombre")

    while True:
        nombre = transformar_audio_texto()
        if nombre != "No te entendí":
            break
        else:
            hablar("No te he entendido nada")
    momento_dia = datetime.datetime.now()
    if nombre != 'Luisi':
        if momento_dia.hour < 6 or momento_dia.hour > 20:
            hablar(f"Hola {nombre}, buenas noches, "
                   f"soy LUISI, tu asistente virtual y personal. ¿En qué puedo ayudarte?")
        elif momento_dia.hour >= 6 and momento_dia.hour < 13:
            hablar(f"Hola {nombre}, buenos días, "
                   f"soy LUISI, tu asistente virtual y personal. ¿En qué puedo ayudarte?")
        else:
            hablar(f"Hola {nombre}, buenas tardes, "
                   f"soy LUISI, tu asistente virtual y personal. ¿En qué puedo ayudarte?")
    else:
        if momento_dia.hour < 6 or momento_dia.hour > 20:
            hablar(f"Hola {nombre}, buenas noches. Yo también me llamo Luisi. Mola")
        elif momento_dia.hour >= 6 and momento_dia.hour < 13:
            hablar(f"Hola {nombre}, buenos días. Yo también me llamo Luisi. Mola")
        else:
            hablar(f"Hola {nombre}, buenas tardes Yo también me llamo Luisi. Mola")
    return nombre



# Función central del asistente
def pedir_cosas():

    nombre = saludo_inicial()

    while True:
        # Activa el micro y guarda la consigna
        consigna = transformar_audio_texto().lower()
        if 'youtube' in consigna:
            hablar(f"{nombre}, Tus deseos son órdenes")
            webbrowser.open("https://www.youtube.com")

        elif 'navegador' in consigna:
            hablar(f"{nombre}, claro que si, ya lo estoy abriendo")
            webbrowser.open("https://www.google.es")

        elif "día es hoy" in consigna:
            pedir_dia()
        elif "hora" in consigna:
            pedir_hora()

        elif 'wikipedia' in consigna:
            hablar(f'{nombre}, claro que si, lo busco')
            consigna = consigna.replace('wikipedia', '')
            wikipedia.set_lang('es')
            resultado = wikipedia.summary(consigna, sentences=1)
            hablar(f"He encontrado esto en Wikipedia: {resultado}")
        elif 'internet' in consigna:
            hablar(f"{nombre}, ya voy")
            consigna = consigna.replace("internet", '')
            pywhatkit.search(consigna)
            hablar("Te lo muestro")
        elif 'reproduce' in consigna:
            hablar("Buena idea. Empieza la reproducción")
            pywhatkit.playonyt(consigna)

        elif 'chiste' in consigna:
            hablar(pyjokes.get_joke('es'))

        elif 'adiós' in consigna:
            hablar(f"{nombre}, Adiós, ha sido un placer. ")
            break




pedir_cosas()