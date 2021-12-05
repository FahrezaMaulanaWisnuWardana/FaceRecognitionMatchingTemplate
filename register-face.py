import cv2
cam = cv2.VideoCapture(0)

cam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while True:
    retV, frame = cam.read()
    cv2.imshow('Pendaftaran Wajah', frame)
    key = cv2.waitKey(1) & 0xFF
    if key == 27 or key == ord('q'):
        break
cam.release()
cv2.destroyAllWindows()
