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

    espejo = cv.flip(imagen, 1)
    espejodecabeza = cv.flip(imagen, -1)
    espejodecabezainvertido = cv.flip(imagen, 0)
    # 0 de cabeza
    # 1 Espejo
    # -1 de cabeza espejo

    cv.imshow("Camara", imagen)
    cv.imshow("Espejo", espejo)
    cv.imshow("De Cabeza", espejodecabeza)
    cv.imshow("De Cabeza Espejo", espejodecabezainvertido)

    # Salgo del programa oprimiendo la tecla ESC
    if cv.waitKey(1) == 27:
        break

camara.release()
cv.destroyAllWindows()