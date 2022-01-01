import cv2
import glob

imdir = 'assets/master/'
ext = ['jpg', 'png']

files = []
[files.extend(glob.glob(imdir + '*.'+e)) for e in ext]

images = [cv2.imread(file) for file in files]

for im in images:
    cv2.imshow("gambar", im)
    cv2.waitKey(0)


# closing all open windows
cv2.destroyAllWindows()
