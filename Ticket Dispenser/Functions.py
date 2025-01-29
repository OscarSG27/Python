# Generadores de turnos

def farmacia():
    for n in range(1, 10000):
        yield f"F-{n}"


def parafarmacia():
    for n in range(1, 10000):
        yield f"P-{n}"


def cosmetica():
    for n in range(1, 10000):
        yield f"C-{n}"


# Asiganción de generadores a variables

f = farmacia()
p = parafarmacia()
c = cosmetica()


# Decorador con el mensaje del ticket

def mensajes_ticket(seccion):
    print("\nSu número es:")
    if seccion == "F":
        print(next(f))
    elif seccion == "P":
        print(next(p))
    else:
        print(next(c))

    print("Espere su turno")


def opciones():
    print("Bienvenid@ a Farmacia Goyo")
    while True:
        print("[F] - Farmacia, [P] - Parafarmacia, [C] - Cosmética")
        try:
            opcion = input("Introduce una opción: ").upper()
            ["P", "C", "F"].index(opcion)
        except ValueError:
            print("Opción no válida.")
        else:
            break

    mensajes_ticket(opcion)


def inicio():
    while True:
        opciones()
        try:
            otro_turno = input("¿Quieres sacar otro turno? [S] [N]: ").upper()
            ["S", "N"].index(otro_turno)
        except ValueError:
            print("Opción no válida.")
        else:
            if otro_turno == "N":
                break
    print("Gracias por su visita")


