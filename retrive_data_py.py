import requests
while(1):
    
    r=requests.get('http://indianiotcloud.com/retrieve.php?id=NQUEES7HH78J9XVFDN29')
    d=r.json()
    print(d)
    d1=d['result'][0]['field1'][1]
    print(d1)
