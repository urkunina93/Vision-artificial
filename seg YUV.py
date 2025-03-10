import cv2
import numpy as np
 
def nothing(x):
    pass
 
cap = cv2.VideoCapture(0)
cv2.namedWindow("Trackbars")
 
cv2.createTrackbar("L - Y", "Trackbars", 0, 179, nothing)
cv2.createTrackbar("L - Cr", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("L - Cb", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("U - Y", "Trackbars", 179, 179, nothing)
cv2.createTrackbar("U - Cr", "Trackbars", 255, 255, nothing)
cv2.createTrackbar("U - Cb", "Trackbars", 255, 255, nothing)
 
 
while True:
    _, frame = cap.read()
    #hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2YCrCb)

    l_h = cv2.getTrackbarPos("L - Y", "Trackbars")
    l_s = cv2.getTrackbarPos("L - Cr", "Trackbars")
    l_v = cv2.getTrackbarPos("L - Cb", "Trackbars")
    u_h = cv2.getTrackbarPos("U - Y", "Trackbars")
    u_s = cv2.getTrackbarPos("U - Cr", "Trackbars")
    u_v = cv2.getTrackbarPos("U - Cb", "Trackbars")
 
    lower_blue = np.array([l_h, l_s, l_v])
    upper_blue = np.array([u_h, u_s, u_v])
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
 
    result = cv2.bitwise_and(frame, frame, mask=mask)
 
    #cv2.imshow("frame", frame)
    #cv2.imshow("mask", mask)
    cv2.imshow("result", result)
 
    key = cv2.waitKey(1)
    if key == 27:
        break
 
cap.release()
cv2.destroyAllWindows()