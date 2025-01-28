class Cliente:
    def __init__(self, nombre, apellido, cuenta_bancaria, balance=0):
        self.nombre = nombre
        self.apellido = apellido
        self.cuenta_bancaria = cuenta_bancaria
        self.balance = balance

    def __str__(self):
        return f"Nombre: {self.nombre} {self.apellido}\nCuenta bancaria: {self.cuenta_bancaria}\n" \
               f"Saldo: {self.balance} €"

    def ingresar(self, saldo_deposito):
        self.balance += saldo_deposito
        print("Ingreso realizado")

    def retirar(self, saldo_retiro):
        if self.balance >= saldo_retiro:
            self.balance -= saldo_retiro
            print("Retiro realizado")
        else:
            print("Fondos no suficientes")


def crear_cliente():
    nombre = input("Introduce tu nombre: ").capitalize()
    apellido = input("Introduce tu apellido: ").capitalize()
    cuenta = input("Introduce tu número de cuenta bancaria: ")

    cliente = Cliente(nombre, apellido, cuenta)

    return cliente


def inicio():
    cliente = crear_cliente()
    print(cliente)
    opcion = 0

    while opcion != "S":
        print("\nElige una opción: Depositar (D), Retirar (R) o Salir (S)")
        opcion = input().upper()

        if opcion == "D":
            saldo_dep = int(input("Introduce el saldo a ingresar: "))
            cliente.ingresar(saldo_dep)
        elif opcion == "R":
            saldo_ret = int(input("Introduce el saldo a retirar: "))
            cliente.retirar(saldo_ret)
        elif opcion == "S":
            break
        else:
            print("Valor introducido no válido")

        print(f"\n{cliente}")

    print("Gracias por operar en Banco XXXX")

