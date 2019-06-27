import cv2
import random
x = int(input('x pos'))
y = int(input('y pos')) 
while(1):
    img = cv2.imread('black.jpg')
    img[x,y,:] =255
    cv2.imshow('image',img)
    k = cv2.waitKey(0)
    if(k==27):
        cv2.destroyAllWindows()
        break
    if(k==97):
        y = random.randrange(1,500)
        
    elif(k==100):
        y = random.randrange(1,200)
    elif(k==115):
        x = random.randrange(1,300)
        
    elif(k==119):
        x = random.randrange(0,300)
        
        
        
        
    
    

