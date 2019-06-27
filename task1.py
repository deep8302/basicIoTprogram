import requests
import random
import time as t
while (True):
    l=(random.sample(range(100),4))
    print(l)
    requests.post('http://indianiotcloud.com/update1.php?id=1DT24SMIX2BHTZM6A4O4&field1='+str(l[0])+'&field2='+str(l[1])+'&field3='+str(l[2])+'&field4='+str(l[3]))
    t.sleep(1)    
         

