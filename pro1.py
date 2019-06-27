import xlrd as x
a=x.open_workbook('medical.xlsx')
b=x.open_workbook('doctor.xlsx')
c=a.sheet_by_index(0)
d=b.sheet_by_index(0)
g=input("How may i help you with:")
if g=="medicine":
    i=input("which medicine:")
    j=int(input('how many:'))
    if i==c.cell_value(1,0):
        k=c.cell_value(1,2)-j
        l=c.cell_value(1,3)*j
        print("used for","=",c.cell_value(1,1))
        print("Quantity available","=",k)
        print("price","=",l)
    elif i==c.cell_value(2,0):
        m=c.cell_value(2,2)-j
        n=c.cell_value(2,3)*j
        print("used for","=",c.cell_value(2,1))
        print("Quantity available","=",c.cell_value(2,2))
        print("price","=",c.cell_value(2,3))
    elif i==c.cell_value(3,0):
        m=c.cell_value(2,2)-j
        n=c.cell_value(2,3)*j
        print("used for","=",c.cell_value(3,1))
        print("Quantity available","=",c.cell_value(3,2))
        print("price","=",c.cell_value(3,3))
    elif i==c.cell_value(4,0):
        m=c.cell_value(2,2)-j
        n=c.cell_value(2,3)*j
        print("used for","=",c.cell_value(4,1))
        print("Quantity available","=",c.cell_value(4,2))
        print("price","=",c.cell_value(4,3))
    elif i==c.cell_value(5,0):
        m=c.cell_value(2,2)-j
        n=c.cell_value(2,3)*j
        print("used for","=",c.cell_value(5,1))
        print("Quantity available","=",c.cell_value(5,2))
        print("price","=",c.cell_value(5,3))
    elif i==c.cell_value(6,0):
        m=c.cell_value(2,2)-j
        n=c.cell_value(2,3)*j
        print("used for","=",c.cell_value(6,1))
        print("Quantity available","=",c.cell_value(6,2))
        print("price","=",c.cell_value(6,3))
    elif i==c.cell_value(7,0):
        m=c.cell_value(2,2)-j
        n=c.cell_value(2,3)*j
        print("used for","=",c.cell_value(7,1))
        print("Quantity available","=",c.cell_value(7,2))
        print("price","=",c.cell_value(7,3))
    else:
        print("sorry,this medicine is not Available")
if g=="doctor":
    input("what are the problems you are having:")
    
    
        
