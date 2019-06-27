import xlrd as x
import time as t
wb=x.open_workbook('Medical.xlsx')
d0=wb.sheet_by_index(0)
d1=wb.sheet_by_index(1)
d2=wb.sheet_by_index(2)

tablet=[ ]
tonic=[ ]
ointment=[ ]
price=[ ]

b=1
bill=0

ch=int(input("SELECT THE TYPE OF MEDICINE YOU WANT TO BUY\n1.TABLET TYPE\n2.TONIC TYPE\n3.OINTMENT TYPE\n"))
