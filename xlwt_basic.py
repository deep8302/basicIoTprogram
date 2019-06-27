#import xlrd as x
import xlwt as x
wb=x.Workbook()
sh1=wb.add_sheet('sheet 1')
#sh1.col(0).width=10000
for i in range(0,11):
    sh1.write(i,0,i)
sh1.write(11,0,x.Formula('SUM(A1:A10)'))
wb.save('qwerty.xls')
