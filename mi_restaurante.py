form tkinter import *


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




                    

