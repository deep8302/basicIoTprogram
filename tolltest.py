import serial
import xlrd as x
wb=x.open_workbook('ttax.xlsx')
s=serial.serial('/dev/ttyUSB0')
s.close()
d=wb.sheet_by_index(0)
c=d.col_values(1)
while(1):
    s.open
    print('port open')
    d=s.read(12)
    print(d)
    s.close()
    for i in range(0,len[c]):
        if(d==c[i]):
            print('access allowed')
        else:
            print('access denied')
            
            
