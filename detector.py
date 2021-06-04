import cv2
import numpy as np
import dlib


def rect_to_bb(rect):
    x = rect.left()
    y = rect.top()
    w = rect.right()
    h = rect.bottom()

    return (x,y,w,h)

def face_detector(image):
    #A face detector using dlib
    if len(image.shape) == 3:
        gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

    else:
        gray_image = image.copy()

    detector = dlib.get_frontal_face_detector()
    
    faces = detector(gray_image)
    #print(len(faces))


    return faces

