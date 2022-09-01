import cv2
import numpy as np

# 카메라 작동하기
cap = cv2.VideoCapture(0)

# 카메라 작동시키기
count = 1
onetime = 1
while True:
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # 가우시안 블러 + 라플라시안 + 캐니 처리하기
    blurred_frame = cv2.GaussianBlur(frame, (5, 5), 0)
    laplacian = cv2.Laplacian(blurred_frame, cv2.CV_64F)
    canny = cv2.Canny(blurred_frame, 100, 150)
    # 사진 띄우기
    if(count == 1):
        if(onetime == 1):
            cv2.destroyAllWindows()
            onetime +=1
        ret, normal = cap.read()
        cv2.imshow("normal", frame)
    elif(count == 2):
        if (onetime == 2):
            cv2.destroyAllWindows()
            onetime += 1
        cv2.imshow("gray", gray)
    elif(count == 3):
        if (onetime == 3):
            cv2.destroyAllWindows()
            onetime += 1
        cv2.imshow("Laplacian", laplacian)
    elif(count == 4):
        if (onetime == 4):
            cv2.destroyAllWindows()
            onetime += 1
        cv2.imshow("Canny", canny)

    key = cv2.waitKey(1)
    if key == ord(' '):
        count += 1;
        if(count == 5):
            count = 1
            onetime = 1
    elif key == 27:
        break

cap.release()
cv2.destroyAllWindows()