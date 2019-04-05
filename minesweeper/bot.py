
import PIL 
from PIL import ImageGrab
import numpy as np  
import win32api     
import cv2


img = cv2.imread('teste2.PNG')

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,80,200,apertureSize = 3)

lines = cv2.HoughLines(edges,1,np.pi/180,200)

print(lines)
for val in lines:
    rho,theta = val[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*(a))
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*(a))

    cv2.line(img,(x1,y1),(x2,y2),(0,0,255),1)



cv2.imshow('a',img)

cv2.waitKey()