from tkinter import *
operador = ''
precios_comida = [1.32, 1.65, 2.31, 3.22, 1.22, 1.99, 2.05, 2,65]
precios_bebidas = [0.25, 0.99, 1.21, 1.54, 1.08, 1.10, 2.00, 1.58]
precios_postres = [1.54, 1.68, 1.32, 1.97, 2.55, 2.14, 1.94, 1.74]


def click_boton(numero):
    global operador
    operador = operador + numero
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(END, operador)

def borrador():
    global operador
    operador = ''
    visor_calculadora.delete(0, END)

def obtener_resultado():
    global operador
    resultado = str(eval(operador))
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(0, resultado)
    operador = ''


def revisar_check():
    x = 0
    for c in cuadros_comida:
        if variables_comida[x].get() == 1:
            cuadros_comida[x].config(state=NORMAL)
            if cuadros_comida[x].get() == '0':
                cuadros_comida[x].delete(0, END)
            cuadros_comida[x].focus()
        else:
            cuadros_comida[x].config(state=DISABLE)
            texto_comida[x].set('0')
        x += 1
    x = 0
    for c in cuadros_bebida:
        if variables_bebida[x].get() == 1:
            cuadros_bebida[x].config(state=NORMAL)
            if cuadros_bebida[x].get() == '0':
                cuadros_bebida[x].delete(0, END)
            cuadros_bebida[x].focus()
        else:
            cuadros_bebida[x].config(state=DISABLED)
            texto_bebida[x].set('0')
        x += 1
    
    x = 0
    for c in cuadros_postres:
        if variable_postres[x].get() == 1:
            cuadros_postres[x]config(state=NORMAL)
            if cuadros_postres[x].get() == '0':
                cuadros_postre[x].delete(0, END)
            cuadros_postres[x].focus()
        else:
            cuadros_postres[x].config(state=DISABLED)
            texto_postres[x].set('0')
        x += 1

def total():
    sub_total_comida = 0
    p = 0
    for cantidad in texto_comida:
        sub_total_comida = sub_total_comida + (float.(cantidad.get()) * precios_comida[])
        p += 1


    sub_total_bebida = 0
    p = 0
    for cantidad in texto_bebida:
        sub_total_bebida = sub_total_bebida + (float.(cantidad.get()) * precios_bebida[])
        p += 1
     

    sub_total_postres = 0
    p = 0
    for cantidad in texto_postres:
        sub_total_postres = sub_total_comida + (float.(cantidad.get()) * precios_postres[])
        p += 1

    sub_total = sub_total_comida + sub_total_bebida+ sub_total_postres
    impuestos = sub_total * 0.07
    total = sub_total + impuestos

    var_costo_comida.set(f'$ {round(sub_total_comida, 2)}')
    var_costo_bebida.set(f'$ {round(sub_total_bebida, 2)}')
    var_costo_postres.set(f'$ {round(sub_total_postres, 2)}')
    var_subtotal.set(f'$ {round(sub_total, 2)}')
    var_impuestos.set(f'$ {round(impuestos, 2)}')
    var_total.set(f'$ {round(total, 2)}')

#FRONTEND

# iniciar tkinter
aplicacion = Tk()

# tamaño de la ventana
aplicacion.geometry('1020x630+0+0')

# evitar maximizar
aplicacion.resizable(0, 0)

# titulo de la ventana
aplicacion.title("Mi Restaurante - Sistema de Facturación")

# color de fondo de la ventana
aplicacion.config(bg='burlywood')

# panel superior
panel_superior = Frame(aplicacion, bd=1, relief=FLAT)
panel_superior.pack(side=TOP)

# etiqueta titulo
etiqueta_titulo = Label(panel_superior, text='Sistema de Facturacion', fg='azure4',
                        font=('Dosis', 58), bg='burlywood', width=27)
etiqueta_titulo.grid(row=0, column=0)

# panel izquierdo
panel_izquierdo = Frame(aplicacion, bd=1, relief=FLAT)
panel_izquierdo.pack(side=LEFT)

# panel costos
panel_costos = Frame(panel_izquierdo, bd=1, relief=FLAT, bg='azure4', padx=50)
panel_costos.pack(side=BOTTOM)

# panel comidas
panel_comidas = LabelFrame(panel_izquierdo, text='Comida', font=('Dosis', 19, 'bold'),
                           bd=1, relief=FLAT, fg='azure4')
panel_comidas.pack(side=LEFT)

# panel bebidas
panel_bebidas = LabelFrame(panel_izquierdo, text='Bebidas', font=('Dosis', 19, 'bold'),
                           bd=1, relief=FLAT, fg='azure4')
panel_bebidas.pack(side=LEFT)

# panel postres
panel_postres = LabelFrame(panel_izquierdo, text='Postres', font=('Dosis', 19, 'bold'),
                           bd=1, relief=FLAT, fg='azure4')
panel_postres.pack(side=LEFT)

# panel derecha
panel_derecha = Frame(aplicacion, bd=1, relief=FLAT)
panel_derecha.pack(side=RIGHT)

# panel calculadora
panel_calculadora = Frame(panel_derecha, bd=1, relief=FLAT, bg='burlywood')
panel_calculadora.pack()

# panel recibo
panel_recibo = Frame(panel_derecha, bd=1, relief=FLAT, bg='burlywood')
panel_recibo.pack()

# panel botones
panel_botones = Frame(panel_derecha, bd=1, relief=FLAT, bg='burlywood')
panel_botones.pack()



# lista de productos
lista_comidas = ['pollo', 'cordero', 'salmon', 'merluza', 'kebab', 'pizza1', 'pizza2', 'pizza3']
lista_bebidas = ['agua', 'soda', 'jugo', 'cola', 'vino1', 'vino2', 'cerveza1', 'cerveza2']
lista_postres = ['helado', 'fruta', 'brownies', 'flan', 'mousse', 'pastel1', 'pastel2', 'pastel3']

# generar items comida
variables_comida = []
cuadros_comida = []
texto_comida = []
contador = 0

for comida in lista_comidas:

    # crear checkbutton
    variables_comida.append('')
    variables_comida[contador] = IntVar()
    comida = Checkbutton(panel_comidas, text=comida.title(), font=('Dosis', 19, 'bold',), onvalue=1, offvalue=0, variable=variables_comida[contador])
    comida.grid(row=contador, column=0, sticky=W)

    # crear los cuadros de entrada comidas
    cuadros_comida.append('')
    texto_comida.append('')
    texto_comida[contador] = StringVar()
    texto_comida[contador].set('0')
    cuadros_comida[contador] = Entry(panel_comidas, font=('Dosis', 18, 'bold'), bd=1, width=6, state=DISABLED, textvariable=texto_comida[contador])
    cuadros_comida[contador].grid(row=contador, column=1)
    contador += 1


# generar items bebida
variables_bebida = []
cuadros_bebida = []
texto_bebida = []
contador = 0

for bebida in lista_bebidas:
    # crear checkbutton
    variables_bebida.append('')
    variables_bebida[contador] = IntVar()
    bebida = Checkbutton(panel_bebidas, text=bebida.title(), font=('Dosis', 19, 'bold',), onvalue=1, offvalue=0, variable=variables_bebida[contador])
    bebida.grid(row=contador, column=0, sticky=W)

    # crear los cuadros de entrada bebidas
    cuadros_bebida.append('')
    texto_bebida.append('')
    texto_bebida[contador] = StringVar()
    texto_bebida[contador].set('0')
    cuadros_bebida[contador] = Entry(panel_bebidas, font=('Dosis', 18, 'bold'), bd=1, width=6, state=DISABLED, textvariable=texto_bebida[contador])
    cuadros_bebida[contador].grid(row=contador, column=1)
    contador += 1

# generar items postres
variables_postres = []
cuadros_postres = []
texto_postres = []
contador = 0

for postres in lista_postres:
    # crear checkbutton
    variables_postres.append('')
    variables_postres[contador] = IntVar()
    postres = Checkbutton(panel_postres, text=postres.title(), font=('Dosis', 19, 'bold'), onvalue=1, offvalue=0, variable=variables_postres[contador])
    postres.grid(row=contador, column=0, sticky=W)

    # crear los cuadros de entrada
    cuadros_postres.append('')
    texto_postres.append('')
    texto_postres[contador] = StringVar()
    texto_postres[contador].set('0')
    cuadros_postres[contador] = Entry(panel_postres, font=('Dosis', 18, 'bold'), bd=1, width=6, state=DISABLED, textvariable=texto_postres[contador])
    cuadros_postres[contador].grid(row=contador, column=1)
    contador += 1

#PANEL RECIBO
# variables
var_costo_comida = StringVar()
var_costo_bebida = StringVar()
var_costo_postres = StringVar()
var_subtotal = StringVar()
var_impuesto = StringVar()
var_total = StringVar()

# Etiquetas de costo y campos de entrada
etiqueta_costo_comida = Label(panel_costos,
                              text='Costo Comida',
                              font=('Dosis', 12, 'bold'),
                              background='azure4',
                              fg='White')
etiqueta_costo_comida.grid(row=0, column=0)
texto_costo_comida = Entry(panel_costos,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_costo_comida)
texto_costo_comida.grid(row=0, column=1, padx=41)

etiqueta_costo_bebida = Label(panel_costos,
                              text='Costo Bebida',
                              font=('Dosis', 12, 'bold'),
                              background='azure4',
                              fg='White')
etiqueta_costo_bebida.grid(row=1, column=0)
texto_costo_bebida = Entry(panel_costos,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_costo_bebida)
texto_costo_bebida.grid(row=1, column=1, padx=41)

etiqueta_costo_postre = Label(panel_costos,
                              text='Costo Postre',
                              font=('Dosis', 12, 'bold'),
                              background='azure4',
                              fg='White')
etiqueta_costo_postre.grid(row=2, column=0)
texto_costo_postre = Entry(panel_costos,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_costo_postres)
texto_costo_postre.grid(row=2, column=1, padx=41)

etiqueta_subtotal = Label(panel_costos,
                              text='Subtotal',
                              font=('Dosis', 12, 'bold'),
                              background='azure4',
                              fg='White')
etiqueta_subtotal.grid(row=0, column=2)
texto_subtotal = Entry(panel_costos,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_subtotal)
texto_subtotal.grid(row=0, column=3, padx=41)

etiqueta_impuestos = Label(panel_costos,
                              text='Impuestos',
                              font=('Dosis', 12, 'bold'),
                              background='azure4',
                              fg='White')
etiqueta_impuestos.grid(row=1, column=2)
texto_impuestos = Entry(panel_costos,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_impuesto)
texto_impuestos.grid(row=1, column=3, padx=41)

etiqueta_total = Label(panel_costos,
                              text='Total',
                              font=('Dosis', 12, 'bold'),
                              background='azure4',
                              fg='White')
etiqueta_total.grid(row=2, column=2)
texto_total = Entry(panel_costos,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_total)
texto_total.grid(row=2, column=3, padx=41)

# botones
botones = ['total','recibo','guardar','resetear']
botones_creados =[]

columnas = 0
for boton in botones:
    boton = Button(panel_botones,
                    text=boton,title(),
                    font=('Dosis',14,'bold'),
                    fg='white',
                    bg='azure4',
                    bd=1,
                    width=9)
    
    botones_creados.append(boton)
    
    boton.grid(row=0,
                column=columnas)
    columnas += 1

botones_creados[0].config(command=total)

#area de recibo
texto_recibo = Text(panel_recibo,
                font=('Donsis', 14, 'bold'),
                    bd=1,
                    width=42,
                    height=10)
texto_recibo.grid(row=0,
                column=0)


# crear los cuadros de entrada

cuadros_comida.append('')
texto_comida.append('')
texto_comida[contador] = StringVar()
texto_comida[contador].set('0')
cuadros_comida[contador] = Entry(panel_bebidas,
                                font=('Dosis, 18, 'bold'),
                                bd=1,
                                width=6,
                                state=DISABLE,
                                textvariable=texto_bebida[contador])
    cuadtos_comida[contador].grid(row=contador,
                                    column=1)
    contador += 1                                

# etiquetas de costo y campos de entrada
etiqueta_costo_comida = Label(panel_costos,
                                text='Costo Comida',
                                font=('Dosis', 12, 'bold'),
                                bf='azure4',
                                fg='white')
etiqueta_costo_comida.grid(row=0, column=0)

texto_costo_comida = Entry(panel_costos,
                            font=('Dosis', 12, 'bold'),
                            bd=1,
                            width=10,
                            state='readonly',
                            textvariable=var_costo_comida)
texto_costo_comida.grid(row=0, column=1, padx=41)

etiqueta_costo_bebida = Label(panel_costos,
                                text='Costo Bebida',
                                font=('Dosis',12,'bold'),
                                bg='azure4',
                                fg='white')
etiqueta_costo_bebida.grid(row=1, column=0)

texto_costo_bebida = Entry(panel_costos,
                            font=('Dosis', 12, 'bold'),
                            bd=1,
                            width=10,
                            state='readonly',
                            textvariable=var_costo_bebida)
texto_costo_bebida.grid(row=1, column=1, padx=41)

etiqueta_costo_postres = Label(panel_costos,
                                text='Costo Bebida',
                                font=('Dosis',12,'bold'),
                                bg='azure4',
                                fg='white')
etiqueta_costo_postres.grid(row=1, column=0)

texto_costo_postres = Entry(panel_costos,
                            font=('Dosis', 12, 'bold'),
                            bd=1,
                            width=10,
                            state='readonly',
                            textvariable=var_costo_bebida)
texto_costo_postres.grid(row=1, column=1, padx=41)

etiqueta_subtotal = Label(panel_costos,
                            text='Subtotal',
                            font=('Dosis', 12, 'bold')
                            bg='azure4',
                            fg='white')
etiqueta_subtotal.grid(row=0, column=2)

etiqueta_impuestos = Label(panel_costos,
                            text='Impuestos',
                            font=('Dosis', 12, 'bold')
                            bg='azure4',
                            fg='white')
etiqueta_impuestos.grid(row=1, column=2)

texto_impuesto = Entry(panel_costos,
                        font=('Dosis', 12, 'bold')
                        bd=1,
                        width=10,
                        state='readonly',
                        textvariable=var_impuestos)
texto_impuestos.grid(row=1,column=3, padx=41)

etiqueta_total = Label(pane_costos,
                        text='Total',
                        font=('Dosis', 12, 'bold')
                        bg='azure4',
                        fg='white')
etiqueta_total.grid(row=2, column=2)

texto_total = Entry(panel_costos,
                        font=('Dosis', 12,  'bold'),
                        bd=1,
                        width=10,
                        state='readonly',
                        textvariable=var_total)
texto_total.grid(row=2, column=3, padx=41)

#BACKEND

#CONFIGURACION CHECKBUTTONS

# comidas
variables_comidas = []
cuadros_comida = []
texto_comida = []
contador = 0
for comida in lista_comidas:
    variables_comidas.append('')
    variables_comidas[contador] = IntVar()
    comida = Checkbutton(panel_comidas, text=comida.title(), font=('Dosis', 19, 'bold'),
                         onvalue=1, offvalue=0, variable=variables_comidas[contador],
                        command = revisar_check)
    
    comida.grid(row=contador, column=0, sticky=W)
    contador += 1

#  bebidas

    variables_bebidas.append('')
    variables_bebidas[contador] = IntVar()
    bebida = Checkbutton(panel_bebidas, text=bebida.title(), font=('Dosis', 19, 'bold'),
                         onvalue=1, offvalue=0, variable=variables_bebidas[contador],
                        command = revisar_check )
    bebida.grid(row=contador, column=0, sticky=W)
    contador += 1

#  postres

    variables_postres.append('')
    variables_postres[contador] = IntVar()
    postre = Checkbutton(panel_postres, text=postre.title(), font=('Dosis', 19, 'bold'),
                         onvalue=1, offvalue=0, variable=variables_postres[contador],
                        command = revisar_check )
    postre.grid(row=contador, column=0, sticky=W)
    contador += 1
    
def revisar_check():
    x = 0
    for c in cuadros_comida:
        if variables_comida[x].get() == 1:
            cuadros_comida[x].config(state=NORMAL)
            cuadros_comida[X].delete(0.END)
            cuadros_comida[X].focus()
        else:
            cuadros_comida[x].config(state=DISABLED)
            texto_comida[X].set('0')  
        X +=1     

    x = 0
    for c in cuadros_bebida:
        if variables_bebida[x].get() == 1:
            cuadros_bebida[x].config(state=NORMAL)
            cuadros_bebida[X].delete(0.END)
            cuadros_bebida[X].focus()
        else:
            cuadros_bebida[x].config(state=DISABLED)
            texto_bebida[X].set('0')  
        X +=1  

    x = 0
    for c in cuadros_postres:
        if variables_postres[x].get() == 1:
            cuadros_postres[x].config(state=NORMAL)
            cuadros_postres[X].delete(0.END)
            cuadros_postres[X].focus()
        else:
            cuadros_postres[x].config(state=DISABLED)
            texto_postres[X].set('0')  
        X +=1  

# evitar que la pantalla se cierre
aplicacion.mainloop()
