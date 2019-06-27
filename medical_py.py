import xlrd as x
wb=x.open_workbook('Medical.xlsx')
d0=wb.sheet_by_index(0)
d1=wb.sheet_by_index(1)
d2=wb.sheet_by_index(2)

nr=d0.nrows
print(nr)

'''nc=d0.ncols
print(nc)

cellvalues=d0.cell_value(0,1)
print(cellvalues)

rowvalues=d0.row_values(0)
print(rowvalues)

columnvalues=d0.col_values(0)
print(columnvalues)'''

'''l0=d0.col_values(0)
l1=d1.col_values(0)
l2=d2.col_values(0)'''

tablet=[ ]
tonic=[ ]
ointment=[ ]
price=[ ]

b=1
bill=0

while(b==1):
    ch=int(input("SELECT THE TYPE OF MEDICINE YOU WANT TO BUY\n1.TABLET TYPE\n2.TONIC TYPE\n3.OINTMENT TYPE\n"))
    if(ch==1):
        a=1
        while(a==1):
            for i in range(0,(nr)):
                l0=d0.row_values(i)
                print(i,l0)
            t1=int(input("SELECT THE TABLET YOU WANT TO BUY:"))
            tablet.append(d0.cell_value(t1,0))
            print("YOU CHOOSE:",tablet)
            print("THIS TEBLET IS PRESENT IN SHELL",(t1,0))
            q1=int(input("ENTER THE QUANTITY:"))
            p=d0.cell_value(t1,1)
            p=q1*p
            price.append(p)
            print("TOTAL PRICE:",price)
            a=int(input("DO YOU WANT TO BUY MORE TABLETS\n1.YES\n2.NO\n"))
            
    elif(ch==2):
       a=1
       while(a==1):
            for i in range(0,(nr)):
                l0=d1.row_values(i)
                print(i,l0)
            t1=int(input("SELECT THE TONIC YOU WANT TO BUY:"))
            tonic.append(d1.cell_value(t1,0))
            print("YOU CHOOSE:",tonic)
            print("THIS TONIC IS PRESENT IN SHELL",(t1,0))
            q1=int(input("ENTER THE QUANTITY:"))
            p=d1.cell_value(t1,1)
            p=q1*p
            price.append(p)
            print("TOTAL PRICE:",price)
            a=int(input("DO YOU WANT TO BUY MORE TONICS\n1.YES\n2.NO\n"))

    elif(ch==3):
       a=1
       while(a==1):
            for i in range(0,(nr)):
                l0=d2.row_values(i)
                print(i,l0)
            t1=int(input("SELECT THE OINTMENT YOU WANT TO BUY:"))
            ointment.append(d2.cell_value(t1,0))
            print("YOU CHOOSE:",ointment)
            print("THIS OINTMENT IS PRESENT IN SHELL",(t1,0))
            q1=int(input("ENTER THE QUANTITY:"))
            p=d2.cell_value(t1,1)
            p=q1*p
            price.append(p)
            print("TOTAL PRICE:",price)
            a=int(input("DO YOU WANT TO BUY MORE OINTMENTS\n1.YES\n2.NO\n"))

    b=int(input("DO YOU WANT TO BUY MORE MEDICINES\n1.YES\n2.NO\n"))
print("\n\n********************BILL INCOICE******************\n\n")
for i in range(0,len(price)):
    bill=bill+price[i]
print("TOTAL BILL:Rs",bill)
    
        
