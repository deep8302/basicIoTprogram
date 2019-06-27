import smtplib as s
import time as t
import randon as r
ch=r.random()
print(ch)
m=s.SMTP('smtp.gmail.com',587)
id='destrothedestroyeer@gmail.com'


name=['vibhu','vatsal','vikas']
password=[123,456,789]
na=input("ENTER YOYR NAME\n")
pwrd=int(input("ENTER YOUR PASSWORD\n"))
for i in range(0,len(name)):
    if(na==name[i]):
        flag=i
        if(pwrd==password[flag]):
            m.starttls()
            m.login(id,"destro_14")
            ch=input("ENTER YOUR EMAIL ID\n")
            m.sendmail(id,ch,'12345')
            m.close()
            otp=input("ENTER THE OTP SENT TO YOUR EMAIL ID:")
            if(otp=='12345'):
                print("LOGIN SUCCESSFULL")
    
            
