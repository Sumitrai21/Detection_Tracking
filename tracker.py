import cv2
import numpy as np




class LucasKanade:
    def __init__(self,old_points):
        #self.old_gray = old_gray
        #self.new_gray = new_gray
        self.old_points = old_points
        self.x = old_points[0]
        self.y = old_points[1]
        #**self.lk_params = **lk_params

    '''
    def forward(self,**lk_parameters):
        if self.new_gray == None:
            pass

        new_points, status,error = cv2.calcOpticalFlowPyrLK(self.old_gray,self.new_gray,self.old_points,None,self.lk_params)

        return new_points,status,error
    '''



def lucas_kanade(old_gray,gray_frame=None,old_points = None):
    # This function uses the lucas kanade optical flow,i.e the tracker
    lk_params = dict(winSize=(10,10),
                maxLevel = 3,
                criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT,10,0.3))
  
    old_points = np.array([old_points],dtype=np.float32)
    new_point,status,error = cv2.calcOpticalFlowPyrLK(old_gray,gray_frame,old_points,None,**lk_params)
    #print(type(new_point))
    x,y = new_point.ravel()
    
    return (x,y),status,error


def draw_circle(frame,points):
    cv2.circle(frame,points,5,(255,0,0),2)


def update_trackers(frame,trackers,old_image,new_image):
    #print('updating the trackers')
    #print(len(trackers))
    try:
        for tracker in trackers:
            #print('inside')
            new_points,status,error = lucas_kanade(old_image,new_image,(tracker.x,tracker.y))
            tracker.x = new_points[0]
            tracker.y = new_points[1]

            #draw_circle(frame,(tracker.x,tracker.y))

        return frame

    except:
        pass

def create_box(trackers,frame,h=30,w=30):
    for tracker in trackers:
        x1 = int(tracker.x - w/2)
        y1 = int(tracker.y -h/2)
        x2 = int(tracker.x + w/2)
        y2 = int(tracker.y + h/2)
        #print(x1,x2,y1,y2)
        cv2.rectangle(frame,(x1,y1),(x2,y2),(0,0,255),2)
        

    return frame






