import os
import time
import sys
a=('abc','def','pqr')
b=(123,456,789)
amt=(4534,353,0)
while(1):
    c=input("\n\nENTER USERID\n")
    if ( c in a):
        for i in range(0,len(a)):
            if (c==a[i]):
                d=int(input("ENTER PASSWORD\n"))
                if(d==b[i]):
                    print("LOGIN SUCCESSFUL\n")
                    ch=int(input("SELECT YOUR CHOICE\n1.WITHDRAWAL\n2.BALANCE ENQUIRY\n3.DEPOSIT\n4.EXIT\n"))
                    if (ch==1):
                        print("YOUR CURRENT AMOUNT IS:",amt[i])
                        e=int(input("ENTER WITHDRAWAL AMOUNT\n"))
                        if(e<=amt[i]):
                            print("WITHDRAWAL SUCCESSFUL\n")
                            rem=amt[i]-e
                            print("YOUR REMAINING BALANCE IS: Rs",rem)
                            print("\nTHANK YOU FOR USING PYTHON ATM\nHAVE A NICE DAY\nLOGGING OUT",end='\r')
                            for m in range(0,3):
                                print('.',end ="\r")
                                time.sleep(1)
                            os.system('cls')
                        else:
                            print("WITHDRAWAL UNSUCCESSFUL\nERROR:LOW BALANCE\n")
                            print("\nTHANK YOU FOR USING PYTHON ATM\nHAVE A NICE DAY\nLOGGING OUT",end='\r')
                            for m in range(0,3):
                                print('.',end="\r")
                                time.sleep(1)
                            os.system('cls')
                    elif (ch==2):
                         print("YOUR ACCOUNT BALANCE IS:",amt[i],"\n")
                         print("\nTHANK YOU FOR USING PYTHON ATM\nHAVE A NICE DAY\nLOGGING OUT",end='\r')
                         for m in range(0,3):
                             print('.',end="\r")
                             time.sleep(1)
                         os.system('cls')
                    elif (ch==3):
                         dep=int(input("ENTER AMOUNT YOU WISH TO DEPOSIT\n"))
                         newamt=amt[i]+dep
                         print("PREVIOUS BALANCE WAS:",amt[i],"NEW BALANCE IS:",newamt,"\n")
                         print("\nTHANK YOU FOR USING PYTHON ATM\nHAVE A NICE DAY\nLOGGING OUT",end='\r')
                         for m in range(0,3):
                             print('.',end="\r")
                             time.sleep(1)
                         os.system('cls')
                    if(ch==4):
                        print("\nTHANK YOU FOR USING PYTHON ATM\nHAVE A NICE DAY\nLOGGING OUT",end='\r')
                        for m in range(0,3):
                            print('.',end="\r")
                            time.sleep(1)
                        exit()
                else:
                    print("INVALID PASSWORD\n")
    else : 
        print("INVALID USER ID\n")
