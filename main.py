import cv2
import numpy as np
import dlib

from detector import face_detector,rect_to_bb
from tracker import LucasKanade, draw_circle, update_trackers
from utils import draw_box





#old_gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
lk_params = dict(winSize=(10,10),
                maxLevel = 2,
                criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT,10,0.3))



trackers = []

def main():
    is_tracker = True
    image = cv2.imread('image.jpg')
    gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    faces = face_detector(image)
    if len(faces) > 0 :
        if is_tracker == True:
            for face in faces:
                x = int((face.left() + face.right())/2)
                y = int((face.top()+face.bottom())/2)
                points = (x,y)
                tracker = LucasKanade(points)
                trackers.append(tracker)

            is_tracker = False
    for tracker in trackers:
        draw_circle(image,(tracker.x,tracker.y))
    #print(len(faces))
    #print(type(faces))
    image = draw_box(image,faces)

    cv2.imshow('frame',image)   
    cv2.waitKey(0)
    

    

    cv2.destroyAllWindows

def test():
    is_tracker = True
    trackers = []
    cap = cv2.VideoCapture(0)
    _,frame = cap.read()
    old_image = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #slow as we have not used numpy yet
    while(cap.isOpened()):
        _,frame = cap.read()
        new_image = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        faces = face_detector(frame)
        frame = draw_box(frame,faces)
        if is_tracker:
            if len(faces)>0:
                for face in faces:
                    x = int((face.left() + face.right())/2)
                    y = int((face.top()+face.bottom())/2)
                    points = (x,y)
                    tracker = LucasKanade(points)
                    trackers.append(tracker)

            is_tracker = False

        frame = update_trackers(frame,trackers,old_image,new_image)
        old_image = new_image.copy()



        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break


    cv2.destroyAllWindows()
    cap.release()


if __name__ == '__main__':
    test()


