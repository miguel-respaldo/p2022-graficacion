import cv2 as cv

camara = cv.VideoCapture(0)

if not camara.isOpened():
    print("No puedo abrir la camara.")
    exit(1)

x=100
y=100

while True:
    # Leeo la imagen de la camara
    retorno, imagen = camara.read()

    if not retorno:
        print("No puedo capturar la imagen de la camara")
        break

    cv.rectangle(imagen, (x,y), (x+100,y+100), (255,0,0), 2)

    cv.imshow("Camara", imagen)

    k=cv.waitKey(1)
    # Salgo del programa oprimiendo la tecla ESC
    if k == 27:
        break
    elif  k == ord("e"): # arriba
        y -= 10
    elif  k == ord("s"): # izquierda
        x -= 10
    elif  k == ord("d"): # abajo
        y += 10
    elif  k == ord("f"): # derecha
        x += 10

camara.release()
cv.destroyAllWindows()
