# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 00:20:26 2021

@author: limon
"""

from tkinter import *
import re

class aplicacion():
    def __init__(self):
        self.raiz = Tk()
        self.raiz.geometry('600x300')
        self.raiz.resizable(width=False, height=False)
        self.raiz.title("EXPRESIONES REGULARES Y CONVERTIDOR BINARIO-DECIMAL")
        label1 = Label(self.raiz, text="VALIDACION DE EXPRESIONES REGULARES")
        label1.pack(padx=10, pady=10)

        self.textos = Frame(self.raiz)
        self.textos.pack(padx=40, pady=10)
        self.frameDeAbajo = Frame(self.raiz)
        self.frameDeAbajo.pack(side=BOTTOM)
        self.t1 = Entry(self.textos, width=40)
        self.t1.grid(row=0, column=0, padx=10, pady=10)

        label2 = Label(self.raiz, text="CONVERTIDOR BINARIO - DECIMAL")
        label2.pack(padx=10, pady=10)
        self.conversor = Frame(self.raiz)
        self.conversor.pack(padx=40, pady=10)
        self.tbinario = Entry(self.conversor, width=20)
        self.tbinario.grid(row=0, column=0, padx=20, pady=1)
        self.tdecimal = Entry(self.conversor, width=20)
        self.tdecimal.grid(row=0, column=2, padx=20, pady=1)

        """""
        self.t2 = Entry(self.textos, width=40)
        self.t2.grid(row=1, column=0)
        self.t3 = Entry(self.textos, width=40)
        self.t3.grid(row=2, column=0)
        self.t4 = Entry(self.textos, width=40)
        self.t4.grid(row=3, column=0)
        """
        self.b1 = Button(self.textos, text='validar', command=lambda: self.validar(1))
        self.b1.grid(row=0, column=1, padx=10, pady=10)
        self.b2 = Button(self.conversor, text='Convertir', command=lambda: self.convertir(1))
        self.b2.grid(row=0, column=1, padx=10, pady=10)
        """""
        self.b2 = Button(self.textos, text='validar', command=lambda: self.validar(2))
        self.b2.grid(row=1, column=1, pady=10)
        self.b3 = Button(self.textos, text='validar', command=lambda: self.validar(3))
        self.b3.grid(row=2, column=1, pady=10)
        self.b4 = Button(self.textos, text='validar', command=lambda: self.validar(4))
        self.b4.grid(row=3, column=1, pady=10)
        """
        self.l1 = Label(self.textos, text='...')
        self.l1.grid(row=0, column=2)
        """
        self.l2 = Label(self.textos, text='...')
        self.l2.grid(row=1, column=2)
        self.l3 = Label(self.textos, text='...')
        self.l3.grid(row=2, column=2)
        self.l4 = Label(self.textos, text='...')
        self.l4.grid(row=3, column=2)
        """
        self.bsalir = Button(self.frameDeAbajo, text="Salir", command=self.raiz.destroy)
        self.bsalir.pack(side=LEFT)
        self.blimpiar = Button(self.frameDeAbajo, text="Limpiar", command=self.limpiar)
        self.blimpiar.pack(side=LEFT)

        self.raiz.mainloop()

    def limpiar(self):
        self.t1.delete(first=0, last='end')
        self.l1.config(fg='black', text='...')
        self.tbinario.delete(first=0, last='end')
        self.tdecimal.delete(first=0, last='end')

    def validar(self, numero):
        if (numero == 1):
            txtAValidar = self.t1.get()
            x = re.search("^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$", txtAValidar)
            if (x):
                self.l1.config(fg="green", text="IPv4 valida")
            else:
                self.l1.config(fg="red", text="IPv4 invalida")

    def convertir(self, valor):
        if (valor == 1):
            txtbinario = self.tbinario.get()
            pos = 0
            dec = 0
            txtbinario = txtbinario[::-1]
            for r in txtbinario:
                mul = 2**pos
                dec += int(r) * mul
                pos += 1
            self.tdecimal.insert(0, str(dec))

        self.raiz.mainloop()

        
app = aplicacion()