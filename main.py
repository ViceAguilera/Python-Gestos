import cv2
from cvzone.HandTrackingModule import HandDetector

#parametros
width, height = 1280, 720

#captura de video
cap = cv2.VideoCapture(0)
cap.set(3, width)
cap.set(4, height)

#detector de manos
detector = HandDetector(detectionCon=0.8, maxHands=1)

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    hands, img = detector.findHands(img)

    if hands:
        hand = hands[0]
        fingers = detector.fingersUp(hand)
        print(fingers)

    cv2.imshow("Video", img)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break