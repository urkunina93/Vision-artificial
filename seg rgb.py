import cv2
import numpy as np

def nothing(x):
    pass

cv2.namedWindow("Trackbars")

# Crear las trackbars para ajustar los rangos de color en RGB
cv2.createTrackbar("L - R", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("L - G", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("L - B", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("U - R", "Trackbars", 255, 255, nothing)
cv2.createTrackbar("U - G", "Trackbars", 255, 255, nothing)
cv2.createTrackbar("U - B", "Trackbars", 255, 255, nothing)

# Cargar imagen
frame = cv2.imread('25.jpg')
if frame is None:
    print("Error: No se pudo cargar la imagen.")
    exit()

while True:
    # Obtener valores de las trackbars
    l_r = cv2.getTrackbarPos("L - R", "Trackbars")
    l_g = cv2.getTrackbarPos("L - G", "Trackbars")
    l_b = cv2.getTrackbarPos("L - B", "Trackbars")
    u_r = cv2.getTrackbarPos("U - R", "Trackbars")
    u_g = cv2.getTrackbarPos("U - G", "Trackbars")
    u_b = cv2.getTrackbarPos("U - B", "Trackbars")

    # Definir los rangos de color en RGB
    lower_bound = np.array([l_b, l_g, l_r])  # OpenCV usa formato BGR
    upper_bound = np.array([u_b, u_g, u_r])

    # Crear la máscara
    mask = cv2.inRange(frame, lower_bound, upper_bound)
    result = cv2.bitwise_and(frame, frame, mask=mask)

    # Mostrar resultados
    cv2.imshow("Original", frame)
    cv2.imshow("Mascara", mask)
    cv2.imshow("Resultado", result)

    # Salir con la tecla 'ESC'
    key = cv2.waitKey(1)
    if key == 27:
        break

cv2.destroyAllWindows()
