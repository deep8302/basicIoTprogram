import xlrd as xr
wbr=xr.open_workbook('hello.xls')
shr=wbr.sheet_by_index(0)
d=d1=shr.col_values(0)
print(d)
flag=0
ch=int(input('ENTER ANY NUMBER\n'))
for i in range (0,len(d)):
    if(ch==(d[i])):
        flag=1

if(flag==1):
     print("VALUE PRESENT")
else:
     print("VALUE NOT PRESENT")
     import xlwt as xw
     wb=xw.Workbook()
     shw=wb.add_sheet('sheet1')
     for i in range(0,len(d1)):
         shw.write(i,0,d1[i])
     shw.write(len(d),0,ch)
     wb.save('hello.xls')
