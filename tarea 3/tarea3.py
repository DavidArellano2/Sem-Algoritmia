# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 23:50:47 2023

@author: David López
"""

import random
import numpy as np
import matplotlib.pyplot as plt
import time
#import matplotlib
from matplotlib.animation import FFMpegWriter
import matplotlib.animation as manimation


#matplotlib.use('TkAgg')
random.seed(10)
np.random.seed(10)


def burbuja(lista):
    iteraciones = 0
    for i in range(1,len(lista)):
        for j in range(0,len(lista)-i):
            iteraciones += 1
            if(lista[j+1] < lista[j]):
                aux=lista[j];
                lista[j]=lista[j+1];
                lista[j+1]=aux;
    return lista, iteraciones

def ordenamientoPorMezcla(lista):
    iteraciones = 0
    if len(lista)>1:
        mitad = len(lista)//2
        mitadIzquierda = lista[:mitad]
        mitadDerecha = lista[mitad:]

        ordenamientoPorMezcla(mitadIzquierda)
        ordenamientoPorMezcla(mitadDerecha)

        i=0
        j=0
        k=0
        while i < len(mitadIzquierda) and j < len(mitadDerecha):
            iteraciones += 1
            if mitadIzquierda[i] < mitadDerecha[j]:
                lista[k]=mitadIzquierda[i]
                i=i+1
            else:
                lista[k]=mitadDerecha[j]
                j=j+1
            k=k+1

        while i < len(mitadIzquierda):
            lista[k]=mitadIzquierda[i]
            i=i+1
            k=k+1

        while j < len(mitadDerecha):
            lista[k]=mitadDerecha[j]
            j=j+1
            k=k+1        
        return lista, iteraciones


elementNumArray=[100,200,400,800,1600,3200,6400,12800,25600,51200,102400,204800,204800*2,204800*4]
elementNumArray=[100,200,400,800,1600,3200,6400,12800]
#elementNumArray=np.arange(100,204800,100)
tiemposBi=[]
iteracionesBi=[]
tiemposLi=[]
iteracionesLi=[]

#FFMpegWriter = manimation.writers['ffmpeg']
metadata = dict(title='OrdenamientoBurbuja Vs OrdenamientoMergeSort', artist='Esteban Ramirez',comment='Tarea 2')
writer = FFMpegWriter(fps=24, metadata=metadata)
fig = plt.figure()
fig, (ax1, ax2) = plt.subplots(1, 2,figsize=(20,10))
ax1.title.set_text('Burbuja')
ax2.title.set_text('MergeSort')
ax1.set_ylabel("Consultas")
ax1.set_xlabel("# Elementos")
ax2.set_xlabel("# Elementos")
with writer.saving(fig, "OrdenamientoBurbujaVsOrdenamientoMergeSort.mp4", 100):

    plt.ion()
    for idx,elementNum in enumerate(elementNumArray):
        lista=np.sort(np.linspace(0,100000,elementNum))
        
        start=time.time()
        elemento,it=burbuja(lista)    
        finish=time.time() 
        iteracionesBi.append(it)
        tiemposBi.append(finish-start)
        
        start=time.time()
        elemento,it=ordenamientoPorMezcla(lista) 
        finish=time.time()
        iteracionesLi.append(it)
        tiemposLi.append(finish-start)
        
        ax1.plot(elementNumArray[:idx+1], iteracionesLi, 'y-',label='Burbuja')
        ax2.plot(elementNumArray[:idx+1], iteracionesBi, 'g-',label='MergeSort')

        fig.canvas.draw()
        fig.canvas.flush_events()
        plt.show(block=False)

        time.sleep(.1)
        for i in range(12):
         writer.grab_frame()

#fig, ax = plt.subplots()
#line1, =ax.plot(elementNumArray,tiempos)
#line1, =ax.plot(elementNumArray,iteraciones)
#plt.show()