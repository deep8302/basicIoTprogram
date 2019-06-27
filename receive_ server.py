import requests as r
import datetime as d
import matplotlib.pyplot as plt
import time as t
plt.ion
values=[]
time=[]
i=0
while(1):
    URL='http://indianiotcloud.com/retrieve.php?id=NQUEES7HH78J9XVFDN29'
    da=r.get(URL)
    data=da.json()
    
    values.append(data['result'][0]['field1'])
    time.append(d.datetime.now().second)
    values.append(data['result'][0]['field2'])
    time.append(d.datetime.now().second)
    values.append(data['result'][0]['field3'])
    time.append(d.datetime.now().second)
    values.append(data['result'][0]['field4'])
    time.append(d.datetime.now().second)
    
    plt.bar([values[i],values[i+1],values[i+2],values[i+3]],[time[i],time[i+1],time[i+2],time[i+3]],.2)
    plt.pause(0.5)
    i=i+4


