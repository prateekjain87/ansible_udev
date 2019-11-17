#!/usr/bin/python36

import cv2

cap = cv2.VideoCapture(0)
ret, image = cap.read()

cv2.imwrite('/my.jpg', image)

cap.release()


