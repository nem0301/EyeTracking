import numpy as np
import cv2
from TrackingPointer import TrackingPointer
import time


width = 1900
height = 1000
font = cv2.FONT_HERSHEY_SIMPLEX

cv2.namedWindow('image', cv2.WINDOW_FULLSCREEN)
while True:    
    pot = TrackingPointer(width, height)
    img = np.zeros((height, width, 3), np.uint8)
    cv2.putText(img,'Select Mode',(50,height/2), font, 4,(255,255,255),2,cv2.LINE_AA)
    cv2.imshow('image', img)
    temp = cv2.waitKey(0)
    
    if temp == ord('q'):
        break
    
    startTime = time.clock()
    timeDuration = 120
    if temp == ord('1'):
        pot.defaultMovementSpeed = 75;
    elif temp == ord('2'):
        pot.defaultMovementSpeed = 45;
    elif temp == ord('3'):
        pot.defaultMovementSpeed = 60;
    elif temp == ord('4'):
        pot.defaultMovementSpeed = 60;
    while cv2.waitKey(1) != 27:
        clockTime = time.clock() - startTime
        minute = int(clockTime) / 60
        second = int(clockTime) % 60
        timeString = str(minute) + " : " + str(second) 
        
        if time.clock() - startTime > timeDuration:
            break        
        
        img = np.zeros((height, width, 3), np.uint8)
        cv2.imshow('image', img)        
        if temp == ord('1'):            
            pot.horizontalMoving()
        
        elif temp == ord('2'):
            pot.veticalMoving()
             
        elif temp == ord('3'):
            pot.diagonalMoving1()
             
        elif temp == ord('4'):
            pot.diagonalMoving2()
            
        elif temp == ord('5'):        
            pot.center()
                 
        else:
            break   
        
        cv2.putText(img, timeString,(50, 50), font, 1,(255,255,255),2,cv2.LINE_AA)
        cv2.circle(img, (int(pot.x), int(pot.y)), 20, (0, 0, 255), -1)
        cv2.imshow('image', img)
        
cv2.destroyAllWindows()              