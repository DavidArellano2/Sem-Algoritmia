import cv2 as cv
import numpy as np
import random as rd
import math

imagenOriginal=cv.imread('fondo.png')
imagenEngris=cv.imread('fondo.png',0)
cv.imshow('imagenen gris',imagenEngris)
cv.imshow('imagen original',imagenOriginal)
cv.waitKey()

print(np.shape(imagenOriginal))
print(np.shape(imagenEngris))
filas,columnas,canales=np.shape(imagenOriginal)
#obteniendo el canal rojo
rojo=np.array(imagenOriginal[:,:,2],dtype='int16')
#obteniendo el canal verde
verde=np.array(imagenOriginal[:,:,1],dtype='int16')
#obteniendo el canal azul
azul=np.array(imagenOriginal[:,:,0],dtype='int16')

#Crear una matriz de ceros con las dimensiones de la imagen
imagenZeros=np.zeros((filas,columnas),dtype='uint8')
#sumarle mas azul a la imagen
menosAzul=np.maximum(imagenZeros,azul-50)
masVerde=np.minimum(255,verde+50)
masRojo=np.minimum(255,rojo+50)
azul=azul.astype('uint8')
verde=verde.astype('uint8')
rojo=rojo.astype('uint8')
menosAzul=menosAzul.astype('uint8')
masVerde=masVerde.astype('uint8')
masRojo=masRojo.astype('uint8')

merged = cv.merge([menosAzul, verde, rojo]) 
#agregarle mas verde a la imagen
merged2 = cv.merge([azul, masVerde, rojo]) 
#imagene con solo el canal rojo
merged3 = cv.merge([imagenZeros, imagenZeros, rojo]) 
cv.imshow('masAzul',merged)
cv.imshow('masVerde',merged2)
cv.imshow('soloRojo',merged3)
cv.waitKey()


#Cambiando la el tamaño de la imagen que solo tiene el canal rojo
imagenPeque=cv.resize(merged3,(int(columnas/2),int(filas/2)),interpolation=cv.INTER_NEAREST)
cv.imshow('pequeña',imagenPeque)
imagenGrande=cv.resize(merged3,(int(columnas*2),int(filas*2)),interpolation=cv.INTER_NEAREST)
cv.imshow('grande',imagenGrande)
cv.waitKey()

imagenEngris=cv.resize(imagenEngris,(480,640),interpolation=cv.INTER_NEAREST)
cv.imshow('pequeña',imagenEngris)
#agregando ruido a la imagen
filas,columnas=np.shape(imagenEngris)
for x in range(5000):
    filard=rd.randint(0,filas-1)
    columnard=rd.randint(0,columnas-1)
    ruido=rd.randint(0,255)
    imagenEngris[filard][columnard]=ruido
    
cv.imshow('ruido',imagenEngris)
cv.waitKey()

imagenEngrisParafiltro3x3=imagenEngris.copy()
imagenEngrisParafiltro5x5=imagenEngris.copy()

#filtro de 3x3 a imagen
for fila in range(1,filas-1):
    for columna in range(1,columnas-1):
        suma=0
        for filaK in range(fila-1,fila+2):
            for colK in range(columna-1,columna+2):
                suma=suma+imagenEngris[filaK][colK]
        #print(suma)
        imagenEngrisParafiltro3x3[fila][columna]=suma/9
        
cv.imshow('filtro de medias',imagenEngrisParafiltro3x3)
#filtro de 5x5 a imagen
for fila in range(2,filas-2):
    for columna in range(2,columnas-2):
        suma=0
        for filaK in range(fila-2,fila+3):
            for colK in range(columna-2,columna+3):
                suma=suma+imagenEngris[filaK][colK]
        #print(suma)
        imagenEngrisParafiltro5x5[fila][columna]=suma/25
        
cv.imshow('filtro de medias 5x5',imagenEngrisParafiltro5x5)
cv.waitKey(0)
        
# Procesamiento en escala de grises
def rgb2gray(img):
    h=img.shape[0]
    w=img.shape[1]
    img1=np.zeros((h,w),np.uint8)
    for i in range(h):
        for j in range(w):
            img1[i,j]=0.144*img[i,j,0]+0.587*img[i,j,1]+0.299*img[i,j,1]
    return img1

def gausskernel(size):
    sigma=1.0
    gausskernel=np.zeros((size,size),np.float32)
    for i in range (size):
        for j in range (size):
            norm=math.pow(i-1,2)+pow(j-1,2)
            gausskernel [i, j] = math.exp (-norm / (2 * math.pow (sigma, 2)))
        sum = np.sum (gausskernel) 
        kernel = gausskernel / sum 
    return kernel


 # Filtro gaussiano
def gauss(img):
    h=img.shape[0]
    w=img.shape[1]
    img1=np.zeros((h,w),np.uint8)
    kernel = gausskernel(3) 
    for i in range (1,h-1):
        for j in range (1,w-1):
            sum=0
            for k in range(-1,2):
                for l in range(-1,2):
                    sum += img [i + k, j + l] * kernel [k + 1, l + 1] 
            img1[i,j]=sum
    return img1

image = cv.imread("fondo.png")
grayimage=rgb2gray(image)
gaussimage = gauss(grayimage)
cv.imshow("Imagen Original",image)
cv.imshow("Imagen gris",grayimage)
cv.imshow("Imagen en filtro gauss",gaussimage)
cv.waitKey(0)
cv.destroyAllWindows()
        
