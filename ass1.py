import requests as r
import datetime as da
import time as ti
import matplotlib.pyplot as plt
plt.ion()


while(1):
    URL=' http://indianiotcloud.com/retrieve.php?id=PPURZU1BD7MVC4UU61B7'
    d=r.get(URL)
    data=d.json()
    i=0
    time=[]
    values=[]
    values.append(data['result'][0]['field1'])
    time.append(da.datetime.now().second)

    values.append(data['result'][0]['field2'])
    time.append(da.datetime.now().second)

    values.append(data['result'][0]['field3'])
    time.append(da.datetime.now().second)

    values.append(data['result'][0]['field4'])
    time.append(da.datetime.now().second)

    print(data)
    print(values,':',time)
    
    
    
    
    plt.bar([values[i],values[i+1],values[i+2],values[i+3]],[time[i],time[i+1],time[i+2],time[i+3]],0.2)
    plt.pause(0.05)
    del values
    del time
    

    
