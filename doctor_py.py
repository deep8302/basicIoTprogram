import xlrd as x
wb=x.open_workbook("symptoms.xlsx")
d0=wb.sheet_by_index(0)
sym=[]
p=[]
a=1
flag=[0,0,0,0]
r=[d0.row_values(0),d0.row_values(1),d0.row_values(2),d0.row_values(3)]
while(a==1):
    ch=input('SELECT THE SYMPTOMS FROM THE BELOW LIST\n1.s1\n2.s2\n3.s3\n4.s4\n5.s5\n6.s6\n7.s7\n8.s8\n9.s9\n10.s10\n')
    sym.append(ch)
    a=int(input('WISH TO ENTER MORE SYMPTOMS\n1.YES\n2.NO\n'))
print('ENTERED SYMPTOMS ARE:',sym)
print("PLEASE WAIT SYSTEM IS UNDER PROCESSING")
for j in range(0,len(sym)):   
        if(sym[j] in r[0]):
            flag[0]=flag[0]+1
            
        if(sym[j] in r[1]):
            flag[1]=flag[1]+1
            
        if(sym[j] in r[2]):
            flag[2]=flag[2]+1
            
        if(sym[j] in r[3]):
            flag[3]=flag[3]+1
ch=max(flag)
print(ch)
for i in range(0,len(flag)):
    if(flag[i]==ch):
        print('YOU ARE SUFFERING FROM DISEASE:')
        print(r[i][1])
        print("YOUR PRESCRIPTION FOR THIS DISEASE IS:")
        print(r[i][0])

        
              
