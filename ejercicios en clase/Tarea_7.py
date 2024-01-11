# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Tarea3.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

import cv2 as cv
import numpy as np
#imagenParis = cv.imread('C:\\Users\\limon\\Desktop\\Seminario_de_Algoritmia\\fondo4.jpg.jpg') #lugar donde toma la foto de fondo
webcam = cv.VideoCapture(0)
salida = cv.VideoWriter('Video Salida 2.mp4',cv.VideoWriter_fourcc(*'XVID'),12,(640,480)) #nombre del video

bgr = [25, 208, 25] #177, 208,25
thresh = 70 #margen del color
minBGR = np.array([bgr[0] - thresh, bgr[1] - thresh, bgr[2] - thresh])
maxBGR = np.array([bgr[0] + thresh, bgr[1] + thresh, bgr[2] + thresh])

while (webcam.isOpened()):
    check, frame = webcam.read()
    imagenParis = cv.imread('C:\\Users\\limon\\Desktop\\Seminario_de_Algoritmia\\fondo4.jpg') #lugar donde toma la foto de fondo
    if check == True:
        maskBGR = cv.inRange(frame, minBGR, maxBGR)
        mask_inv = cv.bitwise_not(maskBGR)
        resultBGR = cv.bitwise_and(frame, frame, mask = mask_inv)
        result_inv = cv.bitwise_and(imagenParis, imagenParis, mask = maskBGR)
        total = cv.add(resultBGR, result_inv)
        cv.imshow("Frame", total)
        salida.write(total)
        if cv.waitKey(50) & 0xFF == ord('q'):
            break
    else:
        break
webcam.release()
salida.release()
cv.destroyAllWindows()
"""
imagenPrincipal=cv.imread('C:\\Users\\limon\\Desktop\\Seminario_de_Algoritmia\\principal.jpg')
imagenParis=cv.imread('C:\\Users\\limon\\Desktop\\Seminario_de_Algoritmia\\fondo3.jpg')
cv.imshow('original',imagenPrincipal)
cv.imshow('fondo',imagenParis)
cv.waitKey()

bgr = [55,200,55]
thresh = 55

minBGR = np.array([bgr[0] - thresh, bgr[1] - thresh, bgr[2] - thresh])
maxBGR = np.array([bgr[0] + thresh, bgr[1] + thresh, bgr[2] + thresh])

maskBGR = cv.inRange(imagenPrincipal,minBGR,maxBGR)
mask_inv = cv.bitwise_not(maskBGR)
cv.imshow('mascara',maskBGR)
cv.imshow('mascara_inv',mask_inv)

# kernel = np.ones((5, 5), np.uint8)
# maskBGR=cv.erode(maskBGR,(1,1,1,1,1,1,1,1,1),30)

# cv.imshow('mascara con erode',maskBGR)
resultBGR = cv.bitwise_and(imagenPrincipal,imagenPrincipal, mask=mask_inv)

result_inv = cv.bitwise_and(imagenParis, imagenParis, mask = maskBGR)


cv.imshow('resultado',resultBGR)
cv.imshow('resultado_inv',result_inv)
cv.waitKey()

total=cv.add(resultBGR,result_inv)

cv.imshow('resultado total',total)

cv.imwrite('resultado.jpg',total)
cv.waitKey()
cv.destroyAllWindows()
"""
