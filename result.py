import cv2
import numpy as np
import os
import time
import pandas as pd


def videoList(dir):
    vid  =  os.listdir(dir)
    vid = [dir+"/"+x for x in vid]
    return vid

    

def isFrame(frame_number,frame_list):

    if frame_number in frame_list:
        return True

    return False


def coord(frame_number,frame_list,df):
    x1 = int(df[df['frame_number']==frame_number].xmin)
    y1 = int(df[df['frame_number']==frame_number].ymin)
    x2 = int(df[df['frame_number']==frame_number].xmax)
    y2 = int(df[df['frame_number']==frame_number].ymax)

    return x1,y1,x2,y2


def get_coord(frame_number,video_id,df):
    df = df[df['video_id'] == video_id]
    frame_list = list(df.frame_number)
    if isFrame(frame_number,frame_list):
        print('True')
        x1,y1,x2,y2 = coord(frame_number,frame_list,df)
        print(x1,y1,x2,y2)
        return (x1,y1,x2,y2)

    return None

