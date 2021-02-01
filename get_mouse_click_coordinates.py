import cv2
import numpy as np
import matplotlib as plt
import math

def draw_circle(event,x,y,flags,param):
    global mouseX,mouseY
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img,(x,y),2,(255,0,0),-1)
        mouseX,mouseY = x,y
        print (str(mouseX)+' , '+str(mouseY))

img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_circle)
img = cv2.imread('D:/Fraunhoffer_FLW_data/Cube_hidden_corner_prediction/Paper DATA/Results Evaluation/TestSet1//350deg_w.png')
while(1):
    cv2.imshow('image',img)
    k = cv2.waitKey(20) & 0xFF
    if k == 27:
        break
    elif k == ord('a'):
        print(str(mouseX)+str(mouseY))