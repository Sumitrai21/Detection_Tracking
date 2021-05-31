import cv2
import numpy




class LucasKanade:
    def __init__(self,old_gray,new_gray,old_points):
        self.old_gray = old_gray
        self.new_gray = new_gray
        self.old_points = old_points
        #**self.lk_params = **lk_params


    def forward(self,**lk_parameters):
        if self.new_gray == None:
            pass

        new_points, status,error = cv2.calcOpticalFlowPyrLK(self.old_gray,self.new_gray,self.old_points,None,self.lk_params)

        return new_points,status,error



def lucas_kanade(old_gray,gray_frame=None,old_points = None,**lk_params):
    # This function uses the lucas kanade optical flow,i.e the tracker
    if gray_frame == None:
        pass
    
    new_point,status,error = cv2.calcOpticalFlowPyrLK(old_gray,gray_frame,old_points,None,**lk_params)
    return new_point,status,error
