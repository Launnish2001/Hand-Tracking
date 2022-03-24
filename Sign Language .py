import cv2
import time
import os
import HandTrackingModule as htm

wCam, hCam = 640, 480

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

folderPath = "Signs"
myList = os.listdir(folderPath)
print(myList)



overlayList = []
for imPath in myList:
    image = cv2.imread(f'{folderPath}/{imPath}')
    # print(f'{folderPath}/{imPath}')
    overlayList.append(image)

print(len(overlayList))
pTime = 0
detector = htm.handDetector(detectionCon=0.75)

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lm = detector.findPosition(img, draw=False)

    res = []
    if len(lm) != 0 and len(res) == 0:


        a = [lm[8][1],lm[12][1],lm[16][1],lm[20][1]]
        b = [lm[6][1],lm[10][1],lm[14][1],lm[18][1]]
        #A
        if a[0] < b[0] and a[1] < b[1] and a[2] < b[2] and a[3] < b[3] and lm[4][1] > b[0] and lm[4][1] > b[1] and lm[4][1] > b[2] and lm[4][1] > b[3]:
            img[0:220, 0:220] = overlayList[9]
            res.append('A')
            print('A')


        else:
            print('NONE')
            res.append(0)






        cv2.rectangle(img, (20, 225), (170, 425), (0, 0, 0), cv2.FILLED)
        cv2.putText(img, str(res[0]), (45, 375), cv2.FONT_HERSHEY_PLAIN, 10, (255, 255, 255), 25)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, f'FPS: {int(fps)}', (400, 70), cv2.FONT_HERSHEY_PLAIN,3, (255, 0, 0), 3)



    cv2.imshow("Image", img)
    cv2.waitKey(1)
