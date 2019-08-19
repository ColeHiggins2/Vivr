import cv2
import os
import Vivr as Vivr


def Main():
    img = cv2.imread('img-00.jpg')
    path = '/Users/coleh/Desktop/Vivr/temp'

    i = 0
    while i < 11:
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

    Vivr.Images.video(path, video_name="MyVivr.mp4")
    Vivr.Images.delete_images(path)


if __name__ == "__main__":
    Main()
