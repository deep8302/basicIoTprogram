import smtplib as s

m=s.SMTP('smtp.gmail.com',587)
m.starttls()
id='sender_email_id'
m.login(id,'password')
for i in range(0,2):
    m.sendmail(id,'receiver_email_id','your_message')
print('MAIL SENT')
m.close()
