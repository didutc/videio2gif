import cv2
import os
from PIL import Image
import imageio
import os
import natsort
file = 'Comp.avi'
imagePath = './images/'


if not (os.path.isdir(file)):


    cap = cv2.VideoCapture(file)

    count = 0

    while True:
        ret, image = cap.read()

        if not ret:
            break

        cv2.imwrite(imagePath + "%d.jpg" % count, image)


        count += 1

    cap.release()
path = [f"./images/{i}" for i in os.listdir("./images")]

path = natsort.natsorted(path)

imgs = [ Image.open(i) for i in path]

imageio.mimsave('./images/test.gif', imgs, fps=20)

