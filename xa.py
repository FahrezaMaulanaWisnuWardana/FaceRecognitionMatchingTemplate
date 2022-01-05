import cv2
import glob
import numpy as np
from tkinter import *
import urllib.request
import os
import mysql.connector
import xlsxwriter
import pyfirmata
import time
import csv

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="face-recognition"
)
conn = db.cursor()
# for x in conn:
# workbook = xlsxwriter.Workbook('Excel.xlsx')
# worksheet = workbook.add_worksheet()

imdir = 'assets/master/'
ext = ['jpg', 'png']
files = []
[files.extend(glob.glob(imdir + '*.'+e)) for e in ext]

# url = "http://192.168.43.35/cam-hi.jpg"
cam = cv2.VideoCapture(0)
frame_w = int(cam.get(3))
frame_h = int(cam.get(4))
out = cv2.VideoWriter('test.avi', cv2.VideoWriter_fourcc(
    'M', 'J', 'P', 'G'), 10, (frame_w, frame_h))

templates = []
templatesSizes = []
counter = 0
for file in files:
    templates.append(cv2.imread(file, 0))
    templatesSizes.append(templates[counter].shape[::-1])
    counter += 1

threshold = 0.7

# board = pyfirmata.Arduino('COM8')

# buzzer = board.get_pin()

while True:
    ret, frame = cam.read()
    # img_resp = urllib.request.urlopen(url)
    # imgnp = np.array(bytearray(img_resp.read()), dtype=np.uint8)
    # frame = cv2.imdecode(imgnp, -1)
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
        if detected:
            img_class = scores.index(max(scores))
            res = cv2.matchTemplate(
                img, templates[img_class], cv2.TM_CCOEFF_NORMED)
            # print(res)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
            loc = np.where(res >= 0.9)
            # print(loc)
            # print(min_loc, max_loc)
            loc = np.where(res >= threshold)
            for pt in zip(*loc[::-1]):
                rgb_img = cv2.rectangle(
                    rgb_img, pt, (pt[0] + templatesSizes[img_class][0]+20, pt[1] + templatesSizes[img_class][1]+20), (0, 0, 255), 1)
                name = str(os.path.splitext(
                    os.path.basename(files[img_class]))[0])
                arrExcel = templates[0][0]
            # Text on top left
            position = (10, 50)
            cv2.putText(rgb_img, (os.path.splitext(os.path.basename(files[img_class]))[0]), position,
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)
            # Query thing
            sql = "INSERT INTO absens(nama) VALUES('{0}')".format(name)
            conn.execute(sql)
            print("Inserted", conn.rowcount, "row(s) of data.")
            # board.digital[7].write(1)
            # board.digital[6].write(1)
            # time.sleep(0.3)
            # board.digital[7].write(0)
            # board.digital[6].write(0)
            db.commit()

            with open('template.csv', 'w') as file:
                writer = csv.writer(file)
                writer.writerows(res)

    cv2.imshow('webcam', rgb_img)
    cv2.imshow('result', res)

    k = cv2.waitKey(1) & 0xFF
    if k == 27 or k == ord('q'):
        db.close()
        break

cam.release()
# out.release()
cv2.destroyAllWindows()
