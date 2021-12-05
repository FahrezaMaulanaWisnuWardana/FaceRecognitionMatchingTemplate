import cv2
import tkinter as tk
from tkinter import *
import numpy as np
from PIL import Image, ImageTk
from datetime import datetime
import pathlib


image_counter = 0


def createwidgets():

    global cameraLabel
    cameraLabel = Label(root, bg="steelblue", borderwidth=3, relief="groove")
    cameraLabel.grid(row=1, column=1, padx=10, pady=10, columnspan=2)

    captureBtn = Button(root, text="Capture", bg="Lightblue",
                        width=20, command=popup)
    captureBtn.grid(row=4, column=1, padx=10, pady=10)

    global stopBtn
    stopBtn = Button(root, text="Stop Camera", bg="Lightblue",
                     width=20, command=StopCam)
    stopBtn.grid(row=4, column=2)

    ShowFeed()


def ShowFeed():
    global cameraLabel
    ret, frame = root.cap.read()
    if ret:
        frame = cv2.flip(frame, 1)
        faceDetector = cv2.CascadeClassifier(
            'haarcascade_frontalface_default.xml')

        cv2.putText(frame, datetime.now().strftime('%d/%m/%y %H:%M:%S'),
                    (20, 30), cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 255, 255))

        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
        faces = faceDetector.detectMultiScale(cv2image, 1.5, 5)

        global x, y, w, h
        for (x, y, w, h) in faces:
            frame = cv2.rectangle(cv2image, (x, y), (x+w, y+h), (0, 0, 255), 2)

        videoimg = Image.fromarray(cv2image)

        imgtk = ImageTk.PhotoImage(image=videoimg)
        cameraLabel.configure(image=imgtk)
        cameraLabel.imgtk = imgtk
        cameraLabel.after(10, ShowFeed)
    else:
        cameraLabel.configure(image="")


def StopCam():
    root.cap.release()
    stopBtn.configure(text="woke", command=StartCam)
    cameraLabel.configure(text="Camera OFF", padx=50,
                          pady=100, font=("SEGOE UI", 70))


def StartCam():
    stopBtn.configure(text="Stop Camera", command=StopCam)
    CamConfig()
    cameraLabel.configure(text="")
    ShowFeed()


def popup():
    top = Toplevel(root)
    top.geometry("250x200")
    top.title("Popup")
    nameText = Label(top, text="Nama")
    nameText.grid(row=1, padx=10, pady=5)
    global name
    name = Entry(top, width=37)
    name.grid(row=2, padx=10, pady=5)
    captureBtn = Button(top, text="Absen", bg="Lightblue",
                        width=20, command=captureImg)
    captureBtn.grid(row=3, padx=10, pady=5)
    infoText = Label(
        top, text="Dengan menekan tombol absen \n system akan merekam dan mencocokkan \n dengan wajah yang tersimpan \n didalam system")
    infoText.grid(row=4, padx=10, pady=15)


def captureImg():
    global imageLabel
    ret, frame = root.cap.read()
    path = pathlib.Path.cwd() / "assets" / name.get()
    path.mkdir(exist_ok=True)
    img_name = 'assets/'+name.get()+'/'+name.get()+'.jpg'
    abuAbu = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(img_name, abuAbu)

    templateImg = cv2.imread('assets/'+name.get() +
                             '/master/'+name.get()+'.jpg', 0)
    imgProc = cv2.imread(img_name, 0)

    w, h = templateImg.shape[::-1]
    crop = imgProc[y:y+h, x:x+w]
    rows, cols = crop.shape
    cv2.imshow("croped", crop)
    res = cv2.matchTemplate(templateImg, crop, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res >= 0.1)
    for pt in zip(*loc[::-1]):
        cv2.rectangle(templateImg, pt, (pt[0]+w, pt[1]+h), (0, 255, 0), 3)
    cv2.imshow("Template Matching", templateImg)


# Settingan camera

def CamConfig():
    root.cap = cv2.VideoCapture(0)
    width, height = 640, 480
    root.cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    root.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)


root = tk.Tk()
CamConfig()
root.title("Pycam")
root.geometry("668x580")
root.config(background="black")

createwidgets()
root.mainloop()
