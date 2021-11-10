import cv2
import pathlib

name = input("Name : ")
path = pathlib.Path.cwd() / "assets" / name
path.mkdir(exist_ok=True)

cam = cv2.VideoCapture(0)
image_counter = 0

while True:
    retV, frame = cam.read()
    camera = cv2.imshow('webcam', frame)
    # cv2.imshow('webcam-grey', abuAbu)
    k = cv2.waitKey(1) & 0xFF
    if k == 27 or k == ord('q'):
        break
    elif k == 32:
        img_name = "assets/"+name+"/"+name+"-"+str(image_counter)+".jpg"
        mat = cv2.imwrite(img_name, frame)
        gambar = cv2.imread(img_name, 0)
        print(gambar)
        image_counter += 1

cam.release()
cv2.destroyAllWindows()
