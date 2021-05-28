import cv2
import numpy as np
import dlib


def face_detector(gray_image,detector):
    #A face detector using dlib
    faces = detector(gray_image)
    #print(len(faces))
    if len(faces) == 0:
        return 0,0,0,0

    for face in faces:
        x1 = face.left()
        y1 = face.top()
        x2 = face.right()
        y2 = face.bottom()


    return x1,y1,x2,y2

def lucas_kanade(old_gray,gray_frame,old_points,**lk_params):
    # This function uses the lucas kanade optical flow,i.e the tracker
    new_point,status,error = cv2.calcOpticalFlowPyrLK(old_gray,gray_frame,old_points,None,**lk_params)
    return new_point,status,error

cap = cv2.VideoCapture(0)
detector = dlib.get_frontal_face_detector()
_,frame = cap.read()
old_gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
lk_params = dict(winSize=(10,10),
                maxLevel = 2,
                criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT,10,0.3))




point_selected = True
old_points = np.array([[]])
while True:
    _, frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    x1,y1,x2,y2 = face_detector(gray,detector)
    if x1!= 0 :
        if point_selected:
            old_points = np.array([[int((x1+x2)/2),int((y1+y2)/2)]],dtype=np.float32)
            point_selected = False

    #print(old_points)
    new_points,status,error = lucas_kanade(old_gray,gray,old_points,**lk_params)
    cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),3)
    old_gray = gray.copy()
    x,y = new_points.ravel()
    old_points = np.array([[x,y]],dtype=np.float32)
    cv2.circle(frame,(x,y),5,(0,255,0),2)
 

    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()