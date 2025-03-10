import cv2
import numpy as np

drawing = False  # Verdadero si el mouse es presionado
mode = True  # Si es verdadero, dibuje un rectangulo, de lo contrario un circulo
ix, iy = -1, -1
fx, fy = -1, -1

#  funcion de llamado del mouse
def draw_circle(event, x, y, flags, param): # Se declara la funcion
    global ix, iy,fx,fy, drawing, mode  # Defino unas variables globales

    if event == cv2.EVENT_LBUTTONDOWN:  # Se pregunta si se ha presionado el mouse
        drawing = True  # En caso de ser verdado se asigna una variable boleana
        ix, iy = x, y  # Almacenamos la poscion incial en las variales


    elif event == cv2.EVENT_LBUTTONUP:  # Cuando se levante el boton
        drawing = False  # Que ya no dibuje
        fx,fy=x,y
        cv2.rectangle(img, (ix, iy), (fx, fy), (0, 255, 255), 0)

        

img = cv2.imread('killer.jpg')  # Leemos la imagen
height, width = img.shape[:2]  # Obtenemos sus dimensiones
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_circle)  # Muestro las imagenes

print ("precione q para salir")

while 1:
    cv2.imshow('image', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        
        break

cv2.destroyAllWindows()

print (ix,iy)
print(fx,fy)

a,b=1,0
img2 = np.zeros((height, width, 3), np.uint8)  # Creamos una imagen nueva
for i in range(iy, fy):


    for j in range(ix, fx):
    	
    	img2[i, j] = img[i, j]


alto=fy-iy
ancho=fx-ix
translation = np.float32([[1, 0, -ix], [0, 1, -iy]])
img3 = cv2.warpAffine(img2, translation, (ancho, alto))

        
cv2.imshow('imagen_resultado', img3)
cv2.waitKey(0)
cv2.destroyAllWindows()
