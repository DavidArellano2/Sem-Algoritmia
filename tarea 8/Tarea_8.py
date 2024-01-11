import cv2 as cv
video = cv.VideoCapture(0,cv.CAP_DSHOW)
cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv.CascadeClassifier(cascPath)
lentes = cv.imread("lentes.png", cv.IMREAD_UNCHANGED)
lentes = cv.resize(lentes, (250, 180))
cv.waitKey()
while (video.isOpened()):
    check, frame = video.read()
    if check == True:
        frame=cv.flip(frame,1)
        imagenGris = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(imagenGris
                                             , scaleFactor=1.1, 
                                             minNeighbors=5, 
                                             minSize=(30,30))
        for(x,y,w,h) in faces:
            frame = cv.cvtColor(frame, cv.COLOR_BGR2BGRA)
            for w in range(lentes.shape[0]):
                for h in range(lentes.shape[1]):
                    if (lentes[w, h][3] != 0):
                        frame[y + w, x + h] = lentes[w, h]
            #cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),10)
            cv.imshow("TAREA 8. FILTRO DE TIKTOK", frame)
            #salida.write(frame)
        if cv.waitKey(50) & 0xFF == ord('q'):
            break
    else:
        break
video.release()
#salida.release()
cv.destroyAllWindows()