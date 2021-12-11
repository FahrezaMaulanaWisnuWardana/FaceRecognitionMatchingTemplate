import cv2
import numpy as np
import urllib.request
url = "http://192.168.43.35/cam-hi.jpg"

# img = cv2.imread('aku.jpg', 0)
template = cv2.imread('assets/master/1.jpg', 0)
h, w = template.shape

while True:
    img_resp = urllib.request.urlopen(url)
    imgnp = np.array(bytearray(img_resp.read()), dtype=np.uint8)
    frame = cv2.imdecode(imgnp, -1)
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    res = cv2.matchTemplate(gray_frame, template, cv2.TM_CCOEFF_NORMED)
    print(res)
    loc = np.where(res >= 0.8)
    for pt in zip(*loc[::-1]):
        p = cv2.rectangle(frame, pt, (pt[0]+w, pt[1]+h), (0, 255, 0), 1)
    # Menggambar Rectangle dari frame camera , dan membentuk rectangle , dengan warna dan ketebalan
    cv2.imshow("live transmission", frame)

    key = cv2.waitKey(5)
    if key == ord('q'):
        break

cv2.destroyAllWindows()
