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
    #print('hahaha')
    #print(frame_number,frame_list)
    if frame_number in frame_list:
        #print('Y')
        return True
    
    return False


def coord(frame_number,frame_list,mycur):
    if isFrame(frame_number,frame_list):
        for doc in mycur:
            if doc['frame_number'] == frame_number:
                x1 = doc['values']['box']['xmin']
                y1 = doc['values']['box']['ymin']
                x2 = doc['values']['box']['xmax']
                y2 = doc['values']['box']['ymax']
                print(x1,y1,x2,y2)

                return x1,y1,x2,y2


def get_coord(frame_number,frame_list,mycur):
    #print('inside')
    if isFrame(frame_number,frame_list):
        #print('True')
        x1,y1,x2,y2 = coord(frame_number,frame_list,mycur)
        #print(x1,y1,x2,y2)
        return (x1,y1,x2,y2)

    return None

