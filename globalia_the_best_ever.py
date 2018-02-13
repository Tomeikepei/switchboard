# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import filedialog
import os



def abrir():
    try:
        archivo = filedialog.askopenfile()
    except:
        print ("File cannot be opened: ", archivo)
    print(" ")
    lista = list()
    for line in archivo:
        lista.append(line)
        if line.startswith(' 8:00- 9:00'):
            a = lista.index(line)
            b = a + 6
        if line.startswith('14:00-15:00'):
            c = lista.index(line)

    d = (lista[a:b])
    e = (lista[c:])

    txtfinal = open('datos.txt', 'w')
    txtfinal.close()
    txtfinal = open('datos.txt', 'r+')
    txtfinal.writelines(d+e)
    txtfinal.close()
    os.startfile("C:/centralita/datos.txt")

ventana = Tk()
ventana.config(bg="black")
ventana.geometry("500x400")
botonAbrir = Button(ventana, text = "Abrir", command = abrir)
botonAbrir.grid(padx = 250, pady= 200)
botonAbrir.pack()
ventana.mainloop()