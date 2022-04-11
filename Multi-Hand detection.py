import cv2
import time
from cvzone.HandTrackingModule import HandDetector
# Accessing Camera
cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.8, maxHands=2)
pTime = 0
# Algorithm using hand tracking module
while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)
    if len(hands) != 0:
        total = []
        #single hand
        if len(hands) == 1:
            hand1 = hands[0]
            fingers1 = detector.fingersUp(hand1)
            h1 = fingers1.count(1)
            total.append(h1)
        #double hand
        elif len(hands) == 2:
            hand1 = hands[0]
            fingers1 = detector.fingersUp(hand1)
            hand2 = hands[1]
            fingers2 = detector.fingersUp(hand2)
            h1 = fingers1.count(1)
            h2 = fingers2.count(1)
            ht = h1 + h2
            total.append(ht)
        total[0] = str(total[0])
        result = ''.join(total)


        #creating real time image of number shown in fingers
        cv2.rectangle(img, (20, 225), (170, 425), (0, 0, 0), cv2.FILLED)
        cv2.putText(img, str(result), (45, 375), cv2.FONT_HERSHEY_PLAIN,
                    8, (255, 255, 255), 25)


    #webcam fps
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, f'FPS: {int(fps)}', (400, 70), cv2.FONT_HERSHEY_PLAIN,
                3, (255, 0, 0), 3)

    cv2.imshow("Image", img)
    cv2.waitKey(1)
