import requests as r
#import xlrd as xr
#wb=xr.open_workbook('prac.xlsx')
#sh=wb.sheet_by_index(0)
#d0=sh.col_values(0)
li=[1,2,3,4]       
i=0
while(1):
    
    
    #li.append(sh.cell_value(i,0))
    #li.append(sh.cell_value(i+1,0))
    #li.append(sh.cell_value(i+2,0))
    #li.append(sh.cell_value(i+3,0))
    print(li)
    
    l='http://indianiotcloud.com/update1.php?id=NQUEES7HH78J9XVFDN29'
    URL=l+'&field1='+str(li[i])+'&field2='+str(li[i+1])+'&field3='+str(li[i+2])+'&field4='+str(li[i+3])
    
    r.post(URL)
    #i=i+4
    
    
