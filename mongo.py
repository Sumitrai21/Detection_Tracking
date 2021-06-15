import pymongo
from pymongo import MongoClient
import cv2
import pandas as pd
import time
import numpy as np
import csv

from detector import face_detector,rect_to_bb
from tracker import LucasKanade, draw_circle, update_trackers, create_box
from utils import draw_box
from result import get_coord, videoList, get_coord

fields = ['video_id','frame_number','x','y']
rows = []
filename = 'face_tracking.csv'

client= MongoClient(
            "10.128.0.102", username="admin", password="Cby2C5hUTBjLHI17LWdpU8wF"
        )

video_id = 24093273 #23249705
db = client.annotator
cursor = db['test-face'].find({"video_id" : str(video_id)})
mycur = list(cursor)

frame_list = []
for doc in mycur:
    frame_list.append(doc['frame_number'])


is_tracker = True
video_name = '2021_04_05/videos/18-35-52.mp4'
cap = cv2.VideoCapture(video_name)
_, frame = cap.read()
old_gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
frame_number = 0
trackers = []
tracker = LucasKanade((0,0))


while(cap.isOpened()):
    _,frame = cap.read()
    try:
        new_gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    except:
        break
    vals = get_coord(frame_number,frame_list,mycur)
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
    #print(tracker.x,tracker.y)
    frame = update_trackers(frame,trackers,old_gray,new_gray)
    old_gray = new_gray.copy()
    rows.append([video_id,frame_number,tracker.x,tracker.y])
    cv2.imshow('frame',frame)
    time.sleep(0.1)
    frame_number +=1
    #print(frame_number)
    if cv2.waitKey(1) & 0xFF == 27:
        break

with open(filename,'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(rows)

cap.release()
cv2.destroyAllWindows()























































