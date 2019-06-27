import time as t
import os
import sys
for h in range (0,24):
    for m in range (0,60):
        for s in range (0,60):
            if (s<10):
                sa='0'+ chr(s+48)
            else:
                x=s%10
                y=s//10
                sa=chr(y+48)+chr(x+48)
            if (m<10):
                mb='0'+chr(m+48)
            else:
                x=m%10
                y=m//10
                mb=chr(y+48)+chr(x+48)
            if (h<10):
                hc='0'+chr(h+48)
            else:
                x=h%10
                y=h//10
                hc=chr(y+48)+chr(x+48)
            r=hc+':'+mb+':'+sa
            gotoxy(10,20)
            print (r)
            t.sleep(1)
            
