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


def IoU(tracker_image,predicted_image):
    xA = max(tracker_image[0],predicted_image[0])
    yA = max(tracker_image[1],predicted_image[1])
    xB = max(tracker_image[2],predicted_image[2])
    yB = max(tracker_image[3],predicted_image[3])

    interArea = max(0,xB-xA+1)*max(0,yB-yA+1)

    tracker_image_area = (tracker_image[2]-tracker_image[0]+1)*(tracker_image[3]-tracker_image[1]+1)
    predicted_image_area = (predicted_image[2]-predicted_image[0]+1)*(predicted_image[3]-predicted_image[1]+1)

    iou = interArea/ float(tracker_image_area+predicted_image_area-interArea)

    return iou



def compare_boxes(trackers,faces):
    pass



