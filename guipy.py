import tkinter as tk
import cv2
from tkinter import *
from PIL import Image, ImageTk

from guimatch import captureImg


def mainpage():
    global cameralabel
    cameralabel = Label(root, bg="steelblue", borderwidth=3, relief="groove")
    cameralabel.grid(row=1, column=1, padx=10, pady=10, columnspan=2)
    captureBtn = Button(root, text="Capture",
                        bg="Lightblue", width=20, command=popup)
    captureBtn.grid(row=2, column=1, padx=10, pady=10)
    Camera()


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
                        width=20)
    captureBtn.grid(row=3, padx=10, pady=5)
    infoText = Label(
        top, text="Dengan menekan tombol absen \n system akan merekam dan mencocokkan \n dengan wajah yang tersimpan \n didalam system")
    infoText.grid(row=4, padx=10, pady=15)


def Camera():
    ret, frame = root.cap.read()
    frame = cv2.flip(frame, 1)
    camColor = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    videoimg = Image.fromarray(camColor)
    imgtk = ImageTk.PhotoImage(image=videoimg)
    cameralabel.configure(image=imgtk)
    cameralabel.imgtk = imgtk
    cameralabel.after(10, mainpage)


def CamConfig():
    root.cap = cv2.VideoCapture(0)
    w, h = 640, 480
    root.cap.set(cv2.CAP_PROP_FRAME_WIDTH, w)
    root.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, h)


root = tk.Tk()
CamConfig()
root.title("guipy")
# root.geometry("250x200")
root.geometry("670x550")
mainpage()
root.mainloop()
