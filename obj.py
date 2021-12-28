import cv2


    
classNames=[]
classFiles='coco.names'
with open(classFiles,'rt') as f:
  classNames=f.read().rstrip('\n').split('\n')
print(classNames)

configPath = 'yolov4.cfg'
weightPath= 'yolov4.weights'

net = cv2.dnn_DetectionModel(weightPath,configPath)


net.setInputSize(320,320)
net.setInputScale(1.0/127.5)
net.setInputMean((127.5,127.5,127.5))
net.setInputSwapRB(True)

camara = "http://10.10.56.196:8080/video"
cap = cv2.VideoCapture(0)
cap.open(camara)
if not cap.isOpened():
    cap=cv2.VideoCapture(0)
if not cap.isOpened():
    raise IOError("cannot open webcam")

while True:
    ret,img=cap.read()
    classIds,confs,bbox=net.detect(img,confThreshold=0.5)
    print(classIds)
    if(len(classIds)!=0):
        for classId,confidence,box in zip(classIds.flatten(),confs.flatten(),bbox):
            if(len(classIds)<=80):
                cv2.rectangle(img,box,(255,0,0),2)
                cv2.putText(img,classNames[classId],(box[0]+10,box[1]+30),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0))

                
                
    cv2.imshow('output',img)           
    if cv2.waitKey(2)&0xFF ==ord('q'):
        break
        
cap.realease()
cv2.destroyAllWindows()





