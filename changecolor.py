import cv2
import numpy as np

cap = cv2.VideoCapture('test.mp4')

while True:
    ret,frame = cap.read()

    if ret == False:
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_bound = np.array([161, 150, 75])
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
    cv2.imshow("Other", dst)

    if cv2.waitKey(1)&0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()

