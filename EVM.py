admin=123
tv=0
pty_vt=['A','B','C','D']
pty_vti=[0,0,0,0]
for j in range (0,len(pty_vt)):
    pty_vti[j]=0
while(tv != 3):
    ch=int(input("TO WHICH PARTY YOU WISH TO VOTE\n1.PARTY A\n2.PARTY B\n3.PARTY C\n4.PARTY D\n"))
    if(ch==1):
        pty_vti[ch]=pty_vti[ch]+1
    elif(ch==2):
        pty_vti[ch]=pty_vti[ch]+1
    elif(ch==3):
        pty_vti[ch]=pty_vti[ch]+1
    elif(ch==4):
        pty_vti[ch]=pty_vti[ch]+1
        
    tv=pty_vti[0]+pty_vti[1]+pty_vti[2]+pty_vti[3]
    if(tv == 3):
        print("VOTING FINISHED")
passs=int(input("ENTER ADMIN PASSWORD TO SEE THE RESULTS\n"))
if( passs==admin ):
    print("THE RESULT IS:")
    
    for i in range (0,len(pty_vt)):
        print("VOTE OF PARTY",pty_vt[i],pty_vti[i])
    m=max(pty_vti)
    print("THE WINNER IS PARTY:")
    for k in range(0,len(pty_vt)):
        if(m==pty_vti[k]):
            print("PARTY",pty_vt[k])
else:
    print("WROND PASSWORD")
    
        


    
