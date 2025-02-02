

def colision_bala_enemigo(bala, enemigo):

    # Comprobamos si la bala ha tocado al enemigo
    if (bala.x + bala.ancho >= enemigo.x and bala.x <= enemigo.x + enemigo.ancho and
            bala.y + bala.alto >= enemigo.y and bala.y <= enemigo.y + enemigo.alto):
        return True  # Colisión detectada
    return False  # No hay colisión


def colision_enemigo_jugador(jugador, enemigo):

    # Comprobamos si el enemigo ha tocado al jugador
    if (jugador.x + jugador.ancho >= enemigo.x and jugador.x <= enemigo.x + enemigo.ancho and
            jugador.y + jugador.alto >= enemigo.y and jugador.y <= enemigo.y + enemigo.alto):
        return True  # Colisión detectada
    return False  # No hay colisión


