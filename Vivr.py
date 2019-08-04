#Look at life from the other side
#import
import copy
import numpy as np
import cv2
import os
from os.path import exists
from PIL import Image, ImageTk, ImageFilter


#read image in a flip flip image
def flip_image(im):
    org = Image.open(im).convert('RGB')
    new=Image.new("RGB",org.size)
    #print(type(org))
    orgpixels, newpixels = org.load(), new.load()
    for x in range(org.size[0]):
        flipped_x = org.size[0] - x - 1
        for y in range(org.size[1]):
            pixel=orgpixels[x, y]
            newpixels[flipped_x, y] = pixel

#store images
"""
def store_image(im):
    image_list = []
    image = Image.open(im).convert('RGB')
    print(type(image))
    image_list.append(image)
    print(image_list)
"""
#convert to video
def video(image_folder, video_name):
    images = [img for img in os.listdir(image_folder) if img.endswith(".jpeg")]
    print(images)
    frame = cv2.imread(os.path.join(image_folder, images[0]))
    height, width, layers = frame.shape

    video = cv2.VideoWriter(video_name, 0, 3, (width,height))

    for image in images:
        video.write(cv2.imread(os.path.join(image_folder, image)))

    cv2.destroyAllWindows()
    video.release()

#if __name__ == '__main__':
    #image_folder =  '/Users/coleh/Desktop/Flikr/temp'
    #video(image_folder, video_name = "NewVivr.mp4")
