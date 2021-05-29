import cv2

class coordinates():
    def __init__(self,x1,y1,x2,y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2



def draw_box(image,faces):

    if len(faces) == 0:
        return image

    for face in faces:
        x1 = face.left()
        x2 = face.right()
        y1 = face.top()
        y2 = face.bottom()

        cv2.rectangle(image,(x1,y1),(x2,y2),(0,255,0),2)


    return image
