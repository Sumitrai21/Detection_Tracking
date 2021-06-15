import pymongo
from pymongo import MongoClient



client= MongoClient(
            "10.128.0.102", username="admin", password="Cby2C5hUTBjLHI17LWdpU8wF"
        )
#print(client.server_info())

video_id = 23249719
db = client.annotator
cursor = db['face'].find({"video_id" : "22819371"})
mycur = list(cursor)

frame_list = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 32, 33, 34, 35, 37, 38, 39, 40, 42, 43, 44, 45, 46]
frame_number = 0

def coord(frame_number,frame_list,mycur):
    for doc in mycur:
        x1 = doc['values']['box']['xmin']
        y1 = doc['values']['box']['ymin']
        x2 = doc['values']['box']['xmax']
        y2 = doc['values']['box']['ymax']
        print(x1,y1,x2,y2)
        print('new')

        yield x1,y1,x2,y2

for i in range(10):
    x1,y1,x2,y2 = coord(i,frame_list,mycur)
    print(x1,y1,x2,y2)