import RPi.GPIO as rp
import time 
rp.setmode(rp.BOARD)
rp.setwarnings(False)
rp.setup(7,rp.OUT)#trigpin
rp.setup(11,rp.IN)#echopin
    
while(1):
    rp.output(7,1)
    time.sleep(0.0001)
    rp.output(7,0)
    
    while(rp.input(11)==0):
        pass
    st=time.time()
    while(rp.input(11)==1):
        pass
    stopt=time.time()
    t=stopt-st
    d=34300*t*0.5
    print(d)
    time.sleep(1)   
