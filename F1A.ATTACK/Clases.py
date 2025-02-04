import pygame
import random
from pygame import mixer
import funciones as f


class Bala:
    def __init__(self, x, y):
        self.imagen = pygame.image.load("bala.png")
        self.x = x
        self.y = y
        self.y_cambio = 35
        self.x_cambio = 0
        self.visible = False
        self.ancho = 16
        self.alto = 16

    def mover(self):
        if self.visible:
            self.y -= self.y_cambio
            if self.y < -16:
                self.visible = False

    def disparar(self, x):
        if not self.visible:
            self.x = x
            self.y = 650
            self.visible = True

    def dibujar(self, pantalla):
        if self.visible:
            pantalla.blit(self.imagen, (self.x, self.y))


class Jugador:
    def __init__(self, x, y):
        self.imagen = pygame.image.load("racing-car.png")
        self.x = x
        self.y = y
        self.x_cambio = 0
        self.ancho = 64
        self.alto = 64

    def mover(self):
        self.x += self.x_cambio
        # Mantener jugador dentro de los bordes de pantalla
        if self.x <= 0:
            self.x = 0
        elif self.x >= 936:
            self.x = 936

    def dibujar(self, pantalla):
        pantalla.blit(self.imagen, (self.x, self.y))


class Enemigo:
    def __init__(self):
        self.puntuacion = Interfaz()
        self.imagen = pygame.image.load("fia.png")
        self.imagen = pygame.transform.scale(self.imagen, (64, 64))
        self.x = random.randint(0, 936)
        self.y = random.randint(50, 200)
        if self.puntuacion.puntuacion < 100:
            self.x_cambio = 10
        elif self.puntuacion.puntuacion <= 200:
            self.x_cambio = 25
        else:
            self.x_cambio = 35

        self.y_cambio = 50
        self.ancho = 63
        self.alto = 63

    def mover(self):
        self.x += self.x_cambio
        # Mantener enemigo dentro de los bordes de pantalla
        if self.x <= 0:
            if self.puntuacion.puntuacion < 100:
                self.x_cambio = 10
            elif self.puntuacion.puntuacion <= 200:
                self.x_cambio = 25
            else:
                self.x_cambio = 35
            self.y += self.y_cambio
        elif self.x >= 936:
            if self.puntuacion.puntuacion < 100:
                self.x_cambio = -10
            elif self.puntuacion.puntuacion <= 200:
                self.x_cambio = -25
            else:
                self.x_cambio = -35

            self.y += self.y_cambio

    def dibujar(self, pantalla):
        pantalla.blit(self.imagen, (self.x, self.y))


class Interfaz:
    def __init__(self, fuente=None):
        self.fuente = pygame.font.Font(fuente, 32)
        self.fuente_final = pygame.font.Font(fuente, 50)
        self.puntuacion = 0
        self.icono = pygame.image.load("f1.png")
        pygame.display.set_caption("F1A Attack")
        pygame.display.set_icon(self.icono)
        self.fondo = pygame.image.load("fondo.png")

    def mostrar_puntuacion(self, pantalla, x, y):
        texto = self.fuente.render(f"Puntos: {self.puntuacion}", True, (10, 10, 10))
        pantalla.blit(texto, (x, y))

    def dibujar_fondo(self, pantalla):
        pantalla.blit(self.fondo, (0, 0))

    # Función para renderizar texto multilínea

    def renderizar_texto_multilinea(self, texto, fuente, color, x, y, pantalla, espacio=40):
        lineas = texto.split("\n")  # Divide el texto en líneas
        for i, linea in enumerate(lineas):
            superficie_texto = fuente.render(linea, True, color)
            if i == 0:
                x_centrado = 350
                pantalla.blit(superficie_texto, (x_centrado, y + i * 60))
            else:
                x_centrado = 250
                pantalla.blit(superficie_texto, (x_centrado, y + i * espacio))

    # Función para mostrar el texto final
    def texto_final(self, pantalla):
        self.renderizar_texto_multilinea(
            "GAME OVER\n\nI DON'T CONSIDER\nANY MORE\nFORMULA 1\nLIKE A SPORT",
            self.fuente_final, (10, 10, 10), 160, 150, pantalla)


class Juego:
    def __init__(self):
        pygame.init()
        self.pantalla = pygame.display.set_mode((1000, 800))
        self.jugador = Jugador(468, 650)
        self.enemigos = [Enemigo() for _ in range(8)]  # Lista de 8 enemigos
        self.bala = Bala(0, 650)
        self.interfaz = Interfaz("freesansbold.ttf")
        self.ejecutando = True

        # Cargar música de fondo
        pygame.mixer.music.load("f1_theme.mp3")
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)

    def ejecutar(self):
        while self.ejecutando:
            for evento in pygame.event.get():
                # Evento cerrar
                if evento.type == pygame.QUIT:
                    self.ejecutando = False
                # Evento presionar teclas
                if evento.type == pygame.KEYDOWN:
                    # Evaluación de que teclas se presionan
                    if evento.key == pygame.K_LEFT:
                        self.jugador.x_cambio = -20

                    if evento.key == pygame.K_RIGHT:
                        self.jugador.x_cambio = +20

                    if evento.key == pygame.K_SPACE:
                        sonido_disparo = mixer.Sound("laser-gun-81720.mp3")
                        sonido_disparo.set_volume(0.1)
                        sonido_disparo.play()
                        if not self.bala.visible:
                            bala_x = self.jugador.x
                            self.bala.disparar(bala_x)
                # Evento soltar teclas
                if evento.type == pygame.KEYUP:
                    # Evaluación de qué teclas se sueltan
                    if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                        self.jugador.x_cambio = 0

            # Modifica la ubicación del jugador en la pantalla
            self.jugador.mover()

            # Colisiones
            # Colision bala - enemigo
            for enemigo in self.enemigos[:]:
                if f.colision_bala_enemigo(self.bala, enemigo):
                    sonido_golpe = mixer.Sound("golpe-corto-y-suave-44138.mp3")
                    sonido_golpe.set_volume(0.8)
                    sonido_golpe.play()
                    self.bala.y = 650
                    self.bala.visible = False
                    self.interfaz.puntuacion += 1
                    # Colocamos al enemigo en una nueva posición
                    enemigo.x = random.randint(0, 936)
                    enemigo.y = random.randint(20, 300)

            # Colisión enemigo - jugador
            for enemigo in self.enemigos[:]:
                if f.colision_enemigo_jugador(self.jugador, enemigo):
                    # Detener la música de fondo
                    pygame.mixer.music.stop()
                    # Reproducir el sonido de "Game Over"
                    sonido_game_over = mixer.Sound("negative_beeps-6008.mp3")
                    sonido_game_over.set_volume(0.8)
                    sonido_game_over.play()

                    # Solo dejar el enemigo que tocó al jugador y eliminar el resto
                    self.enemigos = [enemigo]

                    # Limpiar la pantalla
                    self.pantalla.fill((0, 0, 0))  # Fondo negro para borrar los enemigos

                    # Dibujar el fondo
                    self.interfaz.dibujar_fondo(self.pantalla)

                    # Dibujar el único enemigo que queda
                    enemigo.dibujar(self.pantalla)

                    # Dibujar el jugador
                    self.jugador.dibujar(self.pantalla)

                    # Mostrar mensaje de Game Over
                    self.interfaz.texto_final(self.pantalla)
                    pygame.display.update()
                    pygame.time.wait(7000)

                    self.ejecutando = False

            self.interfaz.dibujar_fondo(self.pantalla)
            self.jugador.dibujar(self.pantalla)
            for enemigo in self.enemigos:
                enemigo.mover()
                enemigo.dibujar(self.pantalla)
            self.bala.mover()
            self.bala.dibujar(self.pantalla)
            self.interfaz.mostrar_puntuacion(self.pantalla, 150, 10)
            pygame.display.update()

        pygame.quit()


