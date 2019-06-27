import smtplib as s
l1=[]

import xlrd as x
wb=x.open_workbook("emailidpy.xlsx")
sh=wb.sheet_by_index(0)
l1=sh.col_values(1)

m=s.SMTP('smtp.gmail.com',587)
m.starttls()
id='destrothedestroyeer@gmail.com'

m.login(id,'destro_14')
print(l1)
ch=int(input("TO WHOM DO YOU WANT TO SND THE MAIL\n1.VIBHU\n2.VATSAL\n3.AKSHAY\n"))
text=input("ENTER YOUR TEXT HERE\n")
for i in range (1,len(l1)):
    if(ch==i):
        m.sendmail(id,l1[i],text)
print("YOUR MAIL IS SENT") 
    
