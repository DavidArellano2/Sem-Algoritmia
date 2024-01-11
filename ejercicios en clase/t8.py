# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 16:51:08 2023

@author: David López
"""

import cv2 as cv

filtropng = cv.imread("lentes.png", cv.IMREAD_UNCHANGED)
cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv.CascadeClassifier(cascPath)
cap = VideoCapture = cv.VideoCapture(0,cv.CAP_DSHOW)
#salida = cv.VideoWriter('Salida.mp4',cv.VideoWriter_fourcc(*'mp4v'),fps,(int(width),int(height)))

if(not cap.isOpened()):
    print("No se pudo abrir la camara ;(") 
else:
    while True:
        ret, frame = cap.read()
        frame = cv.flip(frame,1)
        imagenGrises = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(imagenGrises,
                                             scaleFactor = 1.1,
                                             minNeighbors = 5,
                                             minSize = (30,30))
    for (x,y,w,h) in faces:
        cv.rectangle(frame(x,y),(x+w,y+h),(255,0,255),5)
        
        #redimensionar imagen de entrada
        resized_filtropng = imutils.resize(filtropng, width = w)
        filas_filtropng = resized_filtropng.shape[0]
        col_filtropng = w
        
        dif = 0
        
        porcion_alto = filas_filtropng // 4
    
    if y - filas_filtropng + porcion_alto >= 0:
      n_frame = frame[y - filas_filtropng + porcion_alto: y + porcion_alto, x: x + w]
    else:
        dif = abs(y - filas_filtropng + porcion_alto)
        n_frame = frame[0: y + porcion_alto, x: x + w]
        
    mask = resized_filtropng[:,:,3]
    mask_inv = cv.bitwise_not(mask)
    bg_black = cb.bitwise_and(resized_filtropng, resized_filtropng, mask = mask)
    bg_black = bg_black[dif:, :, 0:3]
    bg_frame = cv.bitwise_and(n_frame, n_frame, mask = mask_inv[dif:, :])
    
    #sumar 2 imagenes para el fondo ddel video
    result = cv.add(bg_black, bg_frame)
    if y - filas_filtropng + porcion_alto >= 0:
        frame[y - filas_filtropng + porcion_alto: y + porcion_alto, x: x + w] = result
    else:
        frame[0: y + porcion_alto, x: x + w] = result 

cv.imshow('Detecciones',frame)
#salida.write(frame)        

        
        
        
        
        
        
        
        
        
        