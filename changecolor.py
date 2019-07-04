import cv2
import numpy as np
print("H:0~180 S:0~255 V:0~255\n")
print("hsv 시작 범위를 입력하시오.(작은 숫자 넣어야 함)\n")
lH = input("H: ")
lS = input("S: ")
lV= input("V: ")
print("hsv 끝 범위를 입력하시오.(큰 숫자 넣어야 함)\n")
uH= input("H: ")
uS= input("S: ")
uV= input("V: ")

cap = cv2.VideoCapture('test.mp4')

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
out = cv2.VideoWriter('result.mp4',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width,frame_height))



while True:
    ret,frame = cap.read()

    if ret == False:
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_bound = np.array([161, 150, 75])
    #lower_bound = np.array([lH, lS, lV])
    upper_bound = np.array([174,255,255])
    mask_color = cv2.inRange(hsv, lower_bound, upper_bound)
    mask_inv = cv2.bitwise_not(mask_color)
    frame_replace = hsv
    frame_replace[:,:,2] -= 75
    frame_replace[:,:,1] -= 90;
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

