import cv2
import numpy

def lucas_kanade(old_gray,gray_frame,old_points,**lk_params):
    # This function uses the lucas kanade optical flow,i.e the tracker
    new_point,status,error = cv2.calcOpticalFlowPyrLK(old_gray,gray_frame,old_points,None,**lk_params)
    return new_point,status,error