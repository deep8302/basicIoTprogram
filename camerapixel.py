import cv2
import time
v= cv2.VideoCapture(0)
while(1):
    r,img = v.read()
    imm = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    r,k1 = cv2.threshold(imm,75,255,cv2.THRESH_BINARY)
    x,y,z = img.shape
    wcount = 0
    bcount = 0
##    cv2.imshow('image',imm)
    cv2.imshow('binary',k1)
    time.sleep(0.0001)
    for i in range(0,x):
        for j in range(0,y):
            if(k1[i,j]==255):
                wcount+=1
    for i in range(0,x):
        for j in range(0,y):
            if(k1[i,j]==0):
                bcount+=1
    print('no. of white pixels =',wcount)
    print('no of black pixels =',bcount)
    k=cv2.waitKey(5)
    if(k==27):
        cv2.destroyAllWindows()
        break   
