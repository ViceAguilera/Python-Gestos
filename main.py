import cv2
from cvzone.HandTrackingModule import HandDetector
import socket

#parametros
width, height = 1280, 720

#captura de video
cap = cv2.VideoCapture(0)
cap.set(3, width)
cap.set(4, height)

#detector de manos
detector = HandDetector(detectionCon=0.8, maxHands=1)

#comunicacion
com = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverAddress = ('127.0.0.1', 5052)

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    hands, img = detector.findHands(img)
    dataFingers = []

    if hands:
        hand = hands[0]
        fingers = detector.fingersUp(hand)
        #print(fingers)
        lmString = ""
        dataFingers = fingers
        print(dataFingers)

    com.sendto(str.encode(str(dataFingers)), serverAddress)

    cv2.imshow("Video", img)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break