import cv2
import numpy as np

cam = cv2.VideoCapture(0)
# print(video)
frame_w = int(cam.get(3))
frame_h = int(cam.get(4))
out = cv2.VideoWriter('test.avi', cv2.VideoWriter_fourcc(
    'M', 'J', 'P', 'G'), 10, (frame_w, frame_h))

templates = []
templatesSizes = []

templates.append(cv2.imread('1.jpg', 0))
templatesSizes.append(templates[0].shape[::-1])

templates.append(cv2.imread('2.jpg', 0))
templatesSizes.append(templates[1].shape[::-1])

templates.append(cv2.imread('3.jpg', 0))
templatesSizes.append(templates[2].shape[::-1])

# templates.append(cv2.imread('4.jpg', 0))
# templatesSizes.append(templates[3].shape[::-1])

threshold = 0.7
while True:
    ret, frame = cam.read()
    rgb_img = frame
    img = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

    scores = []
    detected = 0

    for i in templates:
        res = cv2.matchTemplate(img, i, cv2.TM_CCOEFF_NORMED)
        loc = np.where(res >= threshold)
        score = 0
        for pt in zip(*loc[::-1]):
            score = score + 1
            detected = 1
        scores.append(score)
        # print(scores)
        if detected:
            img_class = scores.index(max(scores))
            # print(img_class, "img")
            res = cv2.matchTemplate(
                img, templates[img_class], cv2.TM_CCOEFF_NORMED)
            # print(templates)
            loc = np.where(res >= threshold)
            for pt in zip(*loc[::-1]):
                rgb_img = cv2.rectangle(
                    rgb_img, pt, (pt[0] + templatesSizes[img_class][0], pt[1] + templatesSizes[img_class][1]), (0, 0, 255), 1)

            position = (10, 50)
            cv2.putText(rgb_img, ('CHECK' + str(img_class)), position,
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)
    out.write(rgb_img)
    cv2.imshow('webcam', rgb_img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27 or k == ord('q'):
        break

cam.release()
out.release()
cv2.destroyAllWindows()
