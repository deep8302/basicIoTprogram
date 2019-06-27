import RPi.GPIO as rp
import time
rp.setmode(rp.BOARD)
rp.setwarnings(False)
rp.setup(11,rp.OUT)
rp.setup(13,rp.OUT)
rp.setup(31,rp.OUT)
rp.setup(33,rp.OUT)
rp.setup(35,rp.OUT)
rp.setup(37,rp.OUT)
def init(): 
    cmd(0x01)
    cmd(0x02)
    cmd(0x28)
    cmd(0x06)
    cmd(0x0c)
def check(d):
    if((d&0x01)==0):
        rp.output(7,0)
    else:
        rp.output(7,1)
    if((d&0x02)==0):
        rp.output(7,0)
    else:
        rp.output(7,1)
    if((d&0x10)==0):
        rp.output(7,0)
    else:
        rp.output(7,1)
    if((d&0x20)==0):
        rp.output(7,0)
    else:
        rp.output(7,1)
    if((d&0x40)==0):
        rp.output(7,0)
    else:
        rp.output(7,1)
    if((d&0x60)==0):
        rp.output(7,0)
    else:
        rp.output(7,1)
def cmd(c):
    d=c&0xf0
    d=d+0x02
    check(d)
    d=d-0x02
    check(d)
    d=c&0x0f
    d=(d<<4)
    d=d+0x02
    check(d)
    d=d-0x02
    check(d)
def data(d):
    d=c&0xf0
    d=d+0x03
    check(d)
    d=d-0x02
    check(d)
    d=c&0x0f
    d=(d<<4)
    d=d+0x03
    check(d)
    d=d-0x02
    check(d)
    

