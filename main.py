import cv2
import numpy as np
import dlib
import pandas as pd
import time

from detector import face_detector,rect_to_bb
from tracker import LucasKanade, draw_circle, update_trackers, create_box
from utils import draw_box
from result import get_coord, videoList, get_coord





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




def run():
    dir = '2021_04_05/videos'
    vid = videoList(dir)

    df = pd.read_csv('2021_04_05/result.csv')
    video_id = 23249719

    is_tracker = True
    cap = cv2.VideoCapture(vid[4])
    _, frame = cap.read()
    old_gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    frame_number = 0
    trackers = []
    tracker = LucasKanade((0,0))

    while(cap.isOpened()):
        _,frame = cap.read()
        new_gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        vals = get_coord(frame_number,video_id,df)
        if vals ==None:
            pass

        else:
            x1 = vals[0]
            x2 = vals[2]
            y1 = vals[1]
            y2 = vals[3]
            cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)

            if is_tracker:
                x = int((x1+x2)/2)
                y = int((y1+y2)/2)
                points = (x,y)
                tracker = LucasKanade(points)
                trackers.append(tracker)
                is_tracker = False

        draw_circle(frame,(tracker.x,tracker.y))
        frame = update_trackers(frame,trackers,old_gray,new_gray)
        old_gray = new_gray.copy()
        cv2.imshow('frame',frame)
        time.sleep(0.1)
        frame_number +=1
        print(frame_number)
        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

        


    
    





def test():
    is_tracker = True
    trackers = []
    max_faces = 0

    cap = cv2.VideoCapture('test_video.mp4')
    _,frame = cap.read()

    old_image = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #slow as we have not used numpy yet

    size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    fourcc = cv2.VideoWriter_fourcc(*'MPEG')

    

    result = cv2.VideoWriter('result.avi',fourcc,29.0,size)

    while(cap.isOpened()):
        _,frame = cap.read()
        if len(frame.shape) == 0:
            break
        new_image = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        faces = face_detector(frame)
        frame = draw_box(frame,faces)
        if len(faces) > max_faces:
            is_tracker = True
            max_faces = len(faces)

        if is_tracker:
            if len(faces)>0:
                for face in faces:
                    x = int((face.left() + face.right())/2)
                    y = int((face.top()+face.bottom())/2)
                    points = (x,y)
                    tracker = LucasKanade(points)
                    trackers.append(tracker)

            is_tracker = False
        #print("Number of trackers: ",len(trackers))
        frame = update_trackers(frame,trackers,old_image,new_image)
        frame = create_box(trackers,frame,h=60,w=60)
        old_image = new_image.copy()


        result.write(frame)
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break

    result.release()
    cv2.destroyAllWindows()
    cap.release()

def result():
    multiple_tracking()


if __name__ == '__main__':
    run()


