import cv2 as cv

camara = cv.VideoCapture(0)

if not camara.isOpened():
    print("No puedo abrir la camara.")
    exit(1)

while True:
    # Leeo la imagen de la camara
    retorno, imagen = camara.read()

    if not retorno:
        print("No puedo capturar la imagen de la camara")
        break

    cv.imshow("Camara", imagen)

    # Salgo del programa oprimiendo la tecla ESC
    if cv.waitKey(1) == 27:
        break

camara.release()
cv.destroyAllWindows()
