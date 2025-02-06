from tkinter import  *

operador = ''

def click_boton(valor_boton):
    global operador
    operador = operador + valor_boton
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(END, operador)

def borrar():
    global operador
    # operador = ''
    visor_calculadora.delete(0, END)
    operador = ''

def obtener_total():
    global operador
    resultado = str(eval(operador))
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(0, resultado)
    operador = ''


def revisar_check(lista_items, variables_items, texto_items):
  for indice, comida in enumerate(lista_items):
        if variables_items[indice].get() == 1:
            lista_items[indice].config(state=NORMAL)
            lista_items[indice].delete(0, END)
            lista_items[indice].focus()
        else:
            lista_items[indice].config(state=DISABLED)
            texto_items[indice].set('0')



# Iniciar a TKINTER
aplicacion = Tk()

# Tamaño de la ventana
aplicacion.geometry('1020x630+0+0')

# Evitar maximizar
aplicacion.resizable(False, False)

# Título de ventana
aplicacion.title('Mi restaurante - Sistema de facturación')

# Panel superior
panel_superior = Frame(aplicacion, bd=1, relief=FLAT)
panel_superior.pack(side=TOP)

# Etiqueta de título
etiqueta_titulo = Label(panel_superior,text='Sistema de facturación', fg='black', font=('Dosis', 58),
                        bg='burlywood', width=22)
etiqueta_titulo.grid(row=0, column=0)

# Panel izquierdo
panel_izquierdo = Frame(aplicacion, bd=1, relief=FLAT)
panel_izquierdo.pack(side=LEFT)

# Panel de costos
panel_costos = Frame(panel_izquierdo, bd=1, relief=FLAT, bg='azure4', padx=40)
panel_costos.pack(side=BOTTOM)

# Panel comidas
panel_comidas = LabelFrame(panel_izquierdo, text='Comida', font=('Dosis', 19, 'bold'), bd=1, relief=FLAT,
                           fg='azure4')
panel_comidas.pack(side=LEFT)

# Panel Bebidas
panel_bebidas = LabelFrame(panel_izquierdo, text='Bebidas', font=('Dosis', 19, 'bold'), bd=1, relief=FLAT,
                           fg='azure4')
panel_bebidas.pack(side=LEFT)


# Panel Postres
panel_postres = LabelFrame(panel_izquierdo, text='Postres', font=('Dosis', 19, 'bold'), bd=1, relief=FLAT,
                           fg='azure4')
panel_postres.pack(side=LEFT)

# Panel derecha
panel_derecha = Frame(aplicacion, bd=1, relief=FLAT)
panel_derecha.pack(side=RIGHT)

# Panel calculadora
panel_calculadora = Frame(panel_derecha, bd=1, relief=FLAT, bg='burlywood')
panel_calculadora.pack()

# Panel Recibo
panel_recibo = Frame(panel_derecha, bd=1, relief=FLAT, bg='burlywood')
panel_recibo.pack()

# Panel botones
panel_botones = Frame(panel_derecha, bd=1, relief=FLAT, bg='burlywood')
panel_botones.pack()

# Lista de productos
lista_comidas = ['pollo', 'cordero', 'salmon', 'pizza1', 'burger']
lista_bebidas = ['agua', 'cola', 'cerveza', 'vino', 'soda']
lista_postres = ['fruta', 'helado', 'flan', 'tarta', 'Yogur']

# Generar items comidas
variables_comida = []
cuadros_comida = []
texto_comida = []
contador = 0
for com in lista_comidas:
    # Crear los checkButton
    var = IntVar()
    variables_comida.append(var)
    comida = Checkbutton(panel_comidas,
                         text=com.capitalize(),
                         font=('Dosis', 19, 'bold'),
                         onvalue=1,
                         offvalue=0,
                         variable=var,
                         command=lambda: revisar_check(cuadros_comida, variables_comida, texto_comida)
                         )

    comida.grid(row=contador,
                column=0,
                sticky=W)

    # Crear las cantidades
    texto_var = StringVar()
    texto_var.set('0')
    texto_comida.append(texto_var)
    cuadros_comida.append(Entry(panel_comidas, font=('Dosis', 18, 'bold'),
                                bd=1,
                                width=6,
                                state=DISABLED,
                                textvariable= texto_var))
    cuadros_comida[contador].grid(row=contador,
                                  column=1)
    contador += 1

# Generar items bebidas
cuadros_bebidas = []
texto_bebidas = []
variables_bebidas = []
contador = 0
for com in lista_bebidas:
    variables_bebidas.append('')
    variables_bebidas[contador] = IntVar()
    bebidas = Checkbutton(panel_bebidas, text=com.capitalize(), font=('Dosis', 19, 'bold'),
                          onvalue=1, offvalue=0, variable=variables_bebidas[contador],
                          command=lambda: revisar_check(cuadros_bebidas, variables_bebidas, texto_bebidas))
    bebidas.grid(row=contador, column=0, sticky=W)

    # Crear las cantidades
    texto_var = StringVar()
    texto_var.set('0')
    texto_bebidas.append(texto_var)
    cuadros_bebidas.append(Entry(panel_bebidas, font=('Dosis', 18, 'bold'),
                                bd=1,
                                width=6,
                                state=DISABLED,
                                textvariable= texto_var))
    cuadros_bebidas[contador].grid(row=contador,
                                   column=1)
    contador += 1


# Generar items postres
cuadros_postres = []
texto_postres = []
variables_postres = []
contador = 0
for com in lista_postres:
    variables_postres.append('')
    variables_postres[contador] = IntVar()
    postres = Checkbutton(panel_postres,
                          text=com.capitalize(),
                          font=('Dosis', 19, 'bold'),
                          onvalue=1, offvalue=0,
                          variable=variables_postres[contador],
                          command=lambda: revisar_check(cuadros_postres, variables_postres, texto_postres))
    postres.grid(row=contador,
                 column=0,
                 sticky=W)

    # Crear las cantidades
    texto_var = StringVar()
    texto_var.set('0')
    texto_postres.append(texto_var)
    cuadros_postres.append(Entry(panel_postres, font=('Dosis', 18, 'bold'),
                                bd=1,
                                width=6,
                                state=DISABLED,
                                textvariable= texto_var))
    cuadros_postres[contador].grid(row=contador,
                                  column=1)
    contador += 1


# Color de fondo
aplicacion.config(bg='burlywood')

# Lista de variables
var_precio_comida = StringVar()
var_precio_bebida = StringVar()
var_precio_postres = StringVar()
var_subtotal = StringVar()
var_iva = StringVar()
var_precio_total = StringVar()

# Etiquetas de precios y campos de entrada

etiqueta_precio_comida = Label(panel_costos,
                               text='Precio Comida',
                               font=('Dosis', 12, 'bold'),
                               bg='azure4',
                               fg='white')
etiqueta_precio_comida.grid(row=0, column=0)
texto_precio_comida = Entry(panel_costos,
                            font=('Dosis', 12, 'bold'),
                            bd=1,
                            width=10,
                            state='readonly',
                            textvariable=var_precio_comida)
texto_precio_comida.grid(row=0, column=1, padx=41)


etiqueta_precio_bebida = Label(panel_costos,
                               text='Precio Bebida',
                               font=('Dosis', 12, 'bold'),
                               bg='azure4',
                               fg='white')
etiqueta_precio_bebida.grid(row=1, column=0)
texto_precio_bebida = Entry(panel_costos,
                            font=('Dosis', 12, 'bold'),
                            bd=1,
                            width=10,
                            state='readonly',
                            textvariable=var_precio_bebida)
texto_precio_bebida.grid(row=1, column=1, padx=41)

etiqueta_precio_postres = Label(panel_costos,
                               text='Precio postres',
                               font=('Dosis', 12, 'bold'),
                               bg='azure4',
                               fg='white')
etiqueta_precio_postres.grid(row=2, column=0)
texto_precio_postres = Entry(panel_costos,
                            font=('Dosis', 12, 'bold'),
                            bd=1,
                            width=10,
                            state='readonly',
                            textvariable=var_precio_postres)
texto_precio_postres.grid(row=2, column=1, padx=41)

subtotal = Label(panel_costos,
                               text='Subtotal',
                               font=('Dosis', 12, 'bold'),
                               bg='azure4',
                               fg='white')
subtotal.grid(row=0, column=2)
texto_subtotal = Entry(panel_costos,
                            font=('Dosis', 12, 'bold'),
                            bd=1,
                            width=10,
                            state='readonly',
                            textvariable=var_subtotal)
texto_subtotal.grid(row=0, column=3, padx=41)

iva = Label(panel_costos,
                               text='IVA',
                               font=('Dosis', 12, 'bold'),
                               bg='azure4',
                               fg='white')
iva.grid(row=1, column=2)
texto_iva = Entry(panel_costos,
                            font=('Dosis', 12, 'bold'),
                            bd=1,
                            width=10,
                            state='readonly',
                            textvariable=var_iva)
texto_iva.grid(row=1, column=3, padx=41)

precio_total = Label(panel_costos,
                               text='Precio Total',
                               font=('Dosis', 12, 'bold'),
                               bg='azure4',
                               fg='white')
precio_total.grid(row=2, column=2)
texto_precio_total = Entry(panel_costos,
                            font=('Dosis', 12, 'bold'),
                            bd=1,
                            width=10,
                            state='readonly',
                            textvariable=var_precio_total)
texto_precio_total.grid(row=2, column=3, padx=41)

# Botones
botones = ['total', 'recibo', 'guardar', 'resetear']
columnas = 0
for boton in botones:
    boton = Button(panel_botones,
                   text=boton.title(),
                   font=('Dosis', 13, 'bold'),
                   fg='white',
                   bg='azure4',
                   bd='1',
                   width=8)
    boton.grid(row=0, column=columnas)
    columnas += 1

# area recibo
texto_recibo = Text(panel_recibo,
                    font=('Dosis', 12, 'bold'),
                    bd=1,
                    width=42,
                    height=10)
texto_recibo.grid(row=0, column=0)

# Calculadora
visor_calculadora = Entry(panel_calculadora,
                          font=('Dosis', 16, 'bold'),
                          width=32,
                          bd=1)
visor_calculadora.grid(row=0, column=0, columnspan=6)
botones_calculadora = ['7', '8', '9', '+', '4', '5', '6', '-', '1', '2', '3', 'X', '=', 'B', '0', '/']
botones_guardados = []
fila = 1
columna = 0
for boton in botones_calculadora:
    boton = Button(panel_calculadora,
                   text=boton.title(),
                   font=('Dosis', 13, 'bold'),
                   fg='white',
                   bg='azure4',
                   bd=1,
                   width=8
                   )
    botones_guardados.append(boton)
    boton.grid(row=fila, column=columna)
    if columna == 3:
        fila += 1
    columna += 1
    if columna == 4:
        columna = 0

for indice, boton in enumerate(botones_calculadora):
    valor = '*' if boton.title() == 'X' else boton.title()

    if valor not in ['B', '=']:
        botones_guardados[indice].config(command=lambda valor_lambda=valor: click_boton(valor_lambda))
    elif valor == 'B':
        botones_guardados[indice].config(command=lambda: borrar())
    elif valor == '=':
        botones_guardados[indice].config(command=lambda: obtener_total())


# Evitar que la pantalla se cierre
aplicacion.mainloop()