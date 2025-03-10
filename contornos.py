import numpy as np
import cv2
 

img = cv2.imread("monedas.jpg")
#img = cv2.imread("monedas1.jpeg")
img = cv2.resize(img,None,fx=0.5, fy=0.5, interpolation = cv2.INTER_CUBIC)
cv2.imshow("Original", img)
gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gauss = cv2.GaussianBlur(gris, (5,5), 0) # Aplicar filtro Gaussiano
ret,thresh = cv2.threshold(gauss,127,255,cv2.THRESH_BINARY| cv2.THRESH_TRIANGLE) # Umbralizacion
(contornos,_) = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) # Buscamos los contornos
cv2.drawContours(img,contornos,-1,(0,0,255), 2) # Dibujamos los contornos

cv2.imshow("Threshold", thresh)
cv2.imshow("Contornos", img)
#cv2.imshow("Filtro", gauss)



print("He encontrado {} objetos".format(len(contornos)))# Mostramos el número de monedas por consola

cv2.waitKey(0)