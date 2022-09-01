import cv2
import sys

src = cv2.VideoCapture('woman.mp4')

if not src.isOpened():
    print('영상 등록 실패')
    sys.exit()

src2 = cv2.VideoCapture('horse.mp4')

if not src2.isOpened():
    print('배경 등록 실패')
    sys.exit()

w = round(src.get(cv2.CAP_PROP_FRAME_WIDTH))
h = round(src.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(w)
print(h)
frame_cnt1 = round(src.get(cv2.CAP_PROP_FRAME_COUNT))
frame_cnt2 = round(src2.get(cv2.CAP_PROP_FRAME_COUNT))
fps = round(src.get(cv2.CAP_PROP_FPS))

delay = int(1000/fps)

do_composit = False

while True:
    ret1, frame1 = src.read()

    if not ret1:
        break

    if do_composit:
        ret2, frame2 = src2.read()

        if not ret2:
            break

        hsv = cv2.cvtColor(frame1, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, (50, 150, 0), (70, 255, 255))
        cv2.copyTo(frame2, mask, frame1)

    cv2.imshow('frame', frame1)
    key = cv2.waitKey(delay)

    if key == ord(' '):
        do_composit = not do_composit
    elif key == 27:
        break

cv2.destroyAllWindows()