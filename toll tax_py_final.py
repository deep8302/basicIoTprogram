import xlrd as xr
import xlwt as xw
import serial
import time as t
import smtplib as sm
import RPi.GPIO as rp
rp.setwarnings(False)
rp.setmode(rp.BOARD)
rp.setup(7,rp.OUT)

wbr=xr.open_workbook('tolltax_excel.xls')
shr=wbr.sheet_by_index(0)
dname=shr.col_values(0)
dcard=shr.col_values(1)
dbal=shr.col_values(2)
demail=shr.col_values(3)
dlist=[dname,dcard,dbal,demail]
nc=shr.ncols

def details(loc):
    print('\nCARD HOLDER NAME:',dname[loc])
    print('CARD NUMBER:',dcard[loc])
    print('CURRENT BALANCE: Rs',dbal[loc])
    wb=xw.Workbook()
    shw=wb.add_sheet('sheet1',cell_overwrite_ok=True)
    for i in range(0,nc):
        for j in range(0,nc):
                   shw.write(j,i,dlist[i][j])
    if(int(dbal[loc])>=50):
        dbal[loc]=dbal[loc]-50
        shw.write(loc,2,dbal[loc])
        print('BALANCE DEDUCTED IS:Rs 50.0')
        print('BALANCE AFTER DEDUCTION IS: Rs',dbal[loc])
        wb.save('tolltax_excel.xls')
        print('THANK YOU',dname[loc],'FOR THE VISIT')
        t.sleep(1)
        rp.output(7,1)
        m=sm.SMTP('smtp.gmail.com',587)
        m.starttls()
        id='destrothedestroyeer@gmail.com'
        receiver_id=demail[loc]
        data='AN AMOUNT OF Rs 50 IS DEDUCTED FROM YOUR CARD NO.-'+str(dcard[loc])+' AVAILABLE BALANCE IS-'+str(dbal[loc])
        m.login(id,'destro_14')
        m.sendmail(id,receiver_id,data)
        print('A MAIL IS SENT TO YOUR REGISTERED EMAIL ID')
        m.close()
    else:
        print('!!!--INSUFFICIENT BALANCE--!!!\n!!!--RECHARGE THE CARD AND TRY AGAIN--!!!')


    

while(1):
    flag=-1
    

    s=serial.Serial('/dev/ttyUSB0')
    s.close()
    s.open()
    print('\nPLEASE SWIPE YOUR CARD')
    number=s.read(12)
    number=number.decode('utf-8')
    for i in range(1,len(dname)):
        if(number==dcard[i]):
            flag=i
    if(flag>-1):
       print('CARD ACCEPTED\nPROCESSING PLEASE WAIT',end='')
       for i in range(0,3):
            t.sleep(1)
            print('.',end='')
       t.sleep(1)
       details(flag)
    else:
        print('CARD UNACCEPTED\nPLEASE TRY AGAIN')
                   




   


    
    
