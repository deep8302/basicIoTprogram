u=('abc','def','pqr')
p=('hey','bye','gone')
v=" "
a=(input('ENTER YOUR USER ID\n'))
if(a in u):
    b=(input("ENTER YOUR PASSWORD\n"))
    for i in range(0,len(p)):
        if(b==p[i]):
            key=int(input("ENTER ENCRYPTION KEY\n"))
            for j in range(0,len(b)):
                c=chr(ord(b[j])+key)
                v=v+c
            print(v)
        else:
            print("WRONG PASSWORD")
else:
    print("INVALID USER ID")
    
