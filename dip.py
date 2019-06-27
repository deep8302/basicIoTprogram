import requests
import matplotlib.pyplot
while (1):
    r=requests.get('http://indianiotcloud.com/retrieve.php?id=APCL3VXNK7PXNB3RT1Z1')
    d=r.json()
    print(d)
    d1=d['result'][0]['field1']
    print(d1)
    d2=d['result'][0]['field2']
    print(d2)
    d3=d['result'][0]['field3']
    print(d3)
    d4=d['result'][0]['field4']
    print(d4)
   
