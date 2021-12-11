import cv2
cam = cv2.VideoCapture('http://192.168.0.105:80/cam.mjpeg')
while True:
    retV, frame = cam.read()
    cv2.imshow('webcam', frame)
    k = cv2.waitKey(1) & 0xFF
    if k == 27 or k == ord('q'):
        break
cam.release()
cv2.destroyAllWindows()
