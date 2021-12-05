import cv2
import numpy as np
from numpy.core.fromnumeric import size
# import tkinter as tk
# from tkinter import *

# Mendeteksi camera bawaan
cap = cv2.VideoCapture(0)
# Gambar Template
template = cv2.imread("assets/reza/master/reza1a.jpg", cv2.IMREAD_GRAYSCALE)
# Mengambil ukuran gambar
w, h = template.shape[::-1]
# print(w, h)

while True:
    # Membaca Camera
    ret, frame = cap.read()
    # merubah gambar dari camera ke dalam warna gray/abu abu
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Proses Template Matching
    res = cv2.matchTemplate(gray_frame, template, cv2.TM_CCORR_NORMED)
    # print(res)
    imgSize = frame.shape
    # print(imgSize)
    # Mengecek kecocokan
    sizeImg = (imgSize[0], imgSize[1])
    loc = np.where(res >= 0.8)
    # for pt in zip(*loc[::-1]):
    # print(pt)
    # Menggambar Rectangle dari frame camera , dan membentuk rectangle , dengan warna dan ketebalan
    p = cv2.rectangle(
        frame, sizeImg, (imgSize[0]+w, imgSize[1]+h), (0, 255, 0), 1)
    print(p)
    cv2.imshow("Template Matching", frame)

    if(cv2.waitKey(5) & 0xFF == ord('q')):
        break

cap.release()
cv2.destroyAllWindows()
