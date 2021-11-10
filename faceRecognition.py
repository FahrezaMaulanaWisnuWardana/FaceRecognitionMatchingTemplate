import PIL
import cv2
import os
from PIL import Image
import numpy as np

DirWajah = 'assets'
trainingData = 'traningWajah'
name = input("Masukkan Nama : ")


def getImageLabel(path):
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    faceSamples = []
    faceIDs = []
    for imagePath in imagePaths:
        PILImg = Image.open(imagePath).convert('L')
        imgNum = np.array(PILImg, 'uint8')
        faceID = str(os.path.split(imagePath)[-1].split(".")[1])
        faces = faceDetector.detectMultiscale(imgNum, 1.3, 5)
        for (x, y, w, h) in faces:
            faceSamples.append(imgNum[y:y+h, x:x+w])
            faceIDs.append(faceID)
            return faceSamples, faceIDs


faceRecognizer = cv2.face.LBPHFaceRecognizer_create()
faceDetector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

faces, IDs = getImageLabel(DirWajah+"/"+name)
faceRecognizer.train(faces, np.array[IDs])

faceRecognizer.write(trainingData+'/'+name+'/training.xml')
