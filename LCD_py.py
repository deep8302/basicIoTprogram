import RPi.GPIO as rp
import time
rp.setwarnings(False)
l=[11,13,31,33,35,37]
rp.setmode(rp.BOARD)
for i in range(0,len(l)):
    rp.setup(l[i],rp.OUT)
li='HELLO'
def clear():
    cmd(0x01)
    time.sleep(0.001)

def init():
    cmd(0x02)
    cmd(0x28)
    cmd(0x06)
    cmd(0x0C)
    cmd(0x85)
    for i in range(0,len(li)):
        data(ord(li[i]))
        time.sleep(2)
    clear()

def cmd(c):
    d=c&0xF0
    d=d+0x02
    checkd(d)
    d=d-0x02
    checkd(d)
    d=(c<<4)&0xF0
    d=d+0x02
    checkd(d)
    d=d-0x02
    checkd(d)

def checkd(c):
    if((c&0x01)==0):
        rp.output(11,0)
    else:
        rp.output(11,1)
        
    if((c&0x02)==0):
        rp.output(13,0)
    else:
        rp.output(13,1)
        
    if((c&0x10)==0):
        rp.output(31,0)
    else:
        rp.output(31,1)
        
    if((c&0x20)==0):
        rp.output(33,0)
    else:
        rp.output(33,1)
        
    if((c&0x40)==0):
        rp.output(35,0)
    else:
        rp.output(35,1)
        
    if((c&0x80)==0):
        rp.output(37,0)
    else:
        rp.output(37,1)

def data(c):
    d=c&0xF0
    d=d+0x03
    checkd(d)
    d=d-0x02
    checkd(d)
    d=(c<<4)&0xF0
    d=d+0x03
    checkd(d)
    d=d-0x02
    checkd(d)

clear()
init()
cmd(0x85)
data(ord('A'))
time.sleep(2)
clear()
    
