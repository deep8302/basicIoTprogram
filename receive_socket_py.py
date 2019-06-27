import socket as s
d=s.socket(s.AF_INET,s.SOCK_DGRAM)
ip='192.168.43.24'
p=1110
d.bind((ip,p))
while(1):
    d,a=d.recvfrom(1024)
    print(d,a)
