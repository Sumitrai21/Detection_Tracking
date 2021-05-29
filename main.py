import cv2
import numpy as np
import dlib

from detector import face_detector,rect_to_bb
from tracker import lucas_kanade
from utils import draw_box





#old_gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
lk_params = dict(winSize=(10,10),
                maxLevel = 2,
                criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT,10,0.3))



def main():
    image = cv2.imread('image.jpg')
    faces = face_detector(image)
    print(len(faces))
    print(type(faces))
    image = draw_box(image,faces)

    cv2.imshow('frame',image)   
    cv2.waitKey(0)
    

    

    cv2.destroyAllWindows


if __name__ == '__main__':
    main()

