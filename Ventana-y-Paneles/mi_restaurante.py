from tkinter import *
import random
import datetime
from tkinter import filedialog, messagebox

def recibo():
    texto_recibo.delete(1.0, END)
    num_recibo = f'N# - {random.randint(1000, 9999)}'
    fecha = datetime.datetime.now()
    fecha_recibo = f'{fecha.day}/{fecha.month}/{fecha.year} - {fecha.hour}: {fecha.minute}'
    texto_recibo.insert(END, f'Datos:\t{num_recibo}\t\t{fecha_recibo}\n')
    texto_recibo.insert(END, f'*' * 47 + '\n')
    texto_recibo.insert(END, 'Items\t\tCant.\tCosto Items\n')
    texto_recibo.insert(END, f'-' * 54'\n')

    x = 0
    for comida in texto_comida:
        if comida.get() != '0':
            texto_recibo.insert(END, f'{lista_comidas[x]}\t\t{comida.get()}\t'
                                f'$ {int(comida.get()) * precios_comida[x]}\n')
        x += 1    

    x = 0
    for bebida in texto_comida:
        if bebida.get() != '0':
            texto_recibo.insert(END, f'{lista_bebidas[x]}\t\t{bebida.get()}\t'
                                f'$ {int(bebida.get()) * precios_bebida[x]}\n')
        x += 1

    x = 0
    for postres in texto_postres:
        if postres.get() != '0':
            texto_recibo.insert(END, f'{lista_postres[x]}\t\t{postres.get()}\t'
                                f'$ {int(postres.get()) * precios_postres[x]}\n')
        x += 1  

    texto_recibo.insert(END, f'-' * 54'\n')
    texto_recibo.insert(END, f' Costo de la Comida: \t\t\t{var_costo_comida.get()}\n')
    texto_recibo.insert(END, f' Costo de la Bebida: \t\t\t{var_costo_bebida.get()}\n')
    texto_recibo.insert(END, f' Costo de la Postres: \t\t\t{var_costo_postres.get()}\n')
    texto_recibo.insert(END, f'-' * 54'\n')
    texto_recibo.insert(END, f' Sub-total : \t\t\t{var_subtotal.get()}\n')
    texto_recibo.insert(END, f' Impuetos: \t\t\t{var_impuesto.get()}\n')
    texto_recibo.insert(END, f' Total : \t\t\t{var_total.get()}\n')
    texto_recibo.insert(END, f'*' * 47 + '\n')
    texto_recibo.insert(END, 'Lo esperamos pronto')

def guardar():
    info_recibo = texto_recibo.get(1.0, END)
    archivo = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    archivo.write(info_recibo)
    archivo.close()
    messagebox.showinfo('Información', 'Su recibo ha sido guardado')


# Panel de Reseteo de Pantalla.

def resetear():
    texto_recibo.delete(0.1, END)

    for texto in texto_comida:
        texto.set('0')
    for texto in texto_bebida:
        texto.set('0')
    for texto in texto_postres:
        texto.set('0')
    
    for cuadro in cuadros_comida:
        cuadro.config(state=DISABLED)
    for cuadro in cuadros_bebida:
        cuadro.config(state=DISABLED)
    for cuadro in cuadros_postres:
        cuadro.config(state=DISABLED)
    
    for v in variables_comida:
        v.set(0)
    for v in variables_bebida:
        v.set(0)
    for v in variables_comida:
        v.set(0)

    var_costo_comida.set('')
    var_costo_bebida.set('')
    var_costo_postres.set('')
    var_subtotal.set('')
    var_impuesto.set('')
    var_total.set('')
    
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
botones = ['total', 'recibo', 'guardar', 'resetear']
columnas = 0
for boton in botones:
    boton = Button(panel_botones,
                   text=boton.title(),
                   font=('Dosis', 14, 'bold'),
                   fg='white',
                   bg='azure4',
                   bd=1,
                   width=9)

    boton.grid(row=0, column=columnas)
    columnas+= 1

botones_creados[0].config(command=total)
botones_creados[1].config(command=recibo)
botones_creados[2].config(command=guardar)
botones_creados[3].config(command=resetear)

# area de recibo
texto_recibo = Text(panel_recibo,
                    font=('Dosis', 12, 'bold'),
                    bd=1,
                    width=42,
                    height=10)
texto_recibo.grid(row=0, column=0)

# evitar que la pantalla se cierre
aplicacion.mainloop()
