import RPi.GPIO as rp
import xlrd as xr
import xlwt as xw
import serial
import time
import smtplib as s
rp.setwarnings(False)
l=[11,31,35]
j=[13,33,37]
rp.setmode(rp.BOARD)
for i in range(0,len(l)):
    rp.setup(l[i],rp.OUT)
for i in range(0,len(j)):
    rp.setup(j[i],rp.IN)
wbr=xr.open_workbook('Format.xlsx')
shr=wbr.sheet_by_index(0)
dname=shr.col_values(0)
dcard=shr.col_values(1)
nc=shr.ncols
s=serial.Serial('/dev/ttyUSB0')
s.open()
d=s.read(12)
for i in range (0,len(dcard)):
    rp.output(16,1)
    time.sleep(0.0001)
    rp.output(16,0)
    while(rp.input(18)==0):
        pass
    st=time.time()
    while(rp.input(18)==1):
        pass
    stopt=time.time()
    t=stopt-st
    d=34300*t/2
    if d==50:     
        print('card accepted')
    elif d==100:
        print('card accepted')
