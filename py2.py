a=('abc','def','pqr')
b=(123,456,789)
c=input("ENTER TEXT HERE\n")
if (c in a):
    d=int(input("ENTER PASSWORD"))
    if(d in b):
        print("login succesfull")
    else:
        print("invalid password")
else:
    print("INVALID USER ID")
