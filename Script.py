import copy
import numpy as np
import cv2
import os
from os.path import exists
from PIL import Image, ImageTk, ImageFilter
import Vivr as Vivr
from PIL import Image


img = cv2.imread('img-00.jpg')
path = '/Users/coleh/Desktop/Vivr/temp'
print(img)
i = 0

while i <11:
    flip = cv2.flip(img, 1)
    cv2.imwrite(os.path.join(path, 'img.%5d.jpeg' % (i)), flip)
    i += 1
    flip = cv2.flip(flip, 1)
    cv2.imwrite(os.path.join(path, 'img.%5d.jpeg' % (i)), flip)
    i += 1
    if i == 4:
        for i in range(4, 8):
                cv2.imwrite(os.path.join(path, 'img.%5d.jpeg' % (i)), img)
                i += 1

Vivr.video(path, video_name = "MyVivr.mp4")

for file in os.scandir(path):
    if file.name.endswith(".jpeg"):
        os.unlink(file.path)
