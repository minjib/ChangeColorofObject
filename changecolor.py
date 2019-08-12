#-*- coding: utf-8 -*-

import cv2
import numpy as np
filename = raw_input("file name: ")
print("H:0~180 S:0~255 V:0~255\n")
#print("hsv 시작 범위를 입력하시오.(작은 숫자 넣어야 함)\n")
print("lower hsv value.(small number)\n")
lH = input("H: ")
lS = input("S: ")
lV= input("V: ")
#print("hsv 끝 범위를 입력하시오.(큰 숫자 넣어야 함)\n")
print("upper hsv value.(big number)\n")
uH= input("H: ")
uS= input("S: ")
uV= input("V: ")
#print("변환활 hsv 값을 입력하시오.(ex.0, -70, 80)\n")
print("input hsv value to change.(eg.0, -70, 80)\n")
cH=0
cS=0
cV=0
cH= int(input("H: "))
cS= int(input("S: "))
cV= int(input("V: "))

cap = cv2.VideoCapture(filename)

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
out = cv2.VideoWriter('result.avi',cv2.VideoWriter_fourcc(*'DIVX'), 30, (frame_width,frame_height))

while True:
    ret,frame = cap.read()

    if ret == False:
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #lower_bound = np.array([6, 112, 41])
    lower_bound = np.array([int(lH), int(lS), int(lV)])
    #upper_bound = np.array([9,206,134])
    upper_bound = np.array([int(uH), int(uS), int(uV)])
    mask_color = cv2.inRange(hsv, lower_bound, upper_bound)
    mask_inv = cv2.bitwise_not(mask_color)
    frame_replace = hsv
    frame_replace[:, :, 0] = frame_replace[:, :, 0]+ cH
    frame_replace[:, :, 1] = frame_replace[:, :, 1]+ cS
    frame_replace[:, :, 2] =frame_replace[:, :, 2]+ cV

    res = cv2.bitwise_and(frame_replace, frame_replace, mask=mask_color)
    res = cv2.cvtColor(res, cv2.COLOR_HSV2BGR)

    other = cv2.bitwise_and(frame, frame, mask=mask_inv)
    dst = cv2.bitwise_or(res, other)
    #cv2.imshow("Other", dst)
    out.write(dst)
    if cv2.waitKey(1)&0xFF == 27:
        break

cap.release()
out.release()
cv2.destroyAllWindows()

