import  xlrd
import datetime as t
name=[]
email=[]
contact=[]
college=[]
branch=[]
year=[]
course=[]
c=0
def details():
    n=input("ENTER YOUR NAME\n")
    name.append(n)
    e=input("ENTER YOUR EMAIL\n")
    email.append(e)
    c=input("ENTER YOUR CONTACT\n")
    contact.append(c)
    co=input("ENTER YOUR COLLEGR\n")
    college.append(co)
    b=input("ENTER YOUR BRANCH\n")
    branch.append(b)
    y=input("ENTER YOUR YEAR\n")
    year.append(y)
    x=input("ENTER ENQUIRY COURSE\n")
    course.append(x)
    review(n,e,c,co,b,y,x)

        
def review(n,e,c,co,b,y,x):
    print("\n\nENTERED DETAILS ARE:")
    print("NAME IS:",n)
    print("EMAIL IS:",e)
    print("CONTACT IS:",c)
    print("COLLEGE IS:",co)
    print("BRANCH IS:",b)
    print("YEAR IS:",y)
    print("ENQUIRED COURSE IS:",x)

        
def enquiry():
    ch=int(input("\n\nSELECT CHOICE TO KNOW ABOUT COURSE \n1.IOT\n2.ML\n3.AI\n4.ROBOTICS\n"))
    if(ch==1):
        print("DETAIL REGARDING IOT COUSE IS:\n#\n##\n###\n####\nTHANK YOU FOR VISITING")
    elif(ch==2):
        print("DETAIL REGARDING ML COUSE IS:\n#\n##\n###\n####\nTHANK YOU FOR VISITING")
    elif(ch==3):
        print("DETAIL REGARDING AI COUSE IS:\n#\n##\n###\n####\nTHANK YOU FOR VISITING")
    elif(ch==4):
        print("DETAIL REGARDING ROBOTICS COUSE IS:\n\n\n\n\nTHANK YOU FOR VISITING")
    else:
        print("WRONG CHOICE\nMAKE A VALID CHOICE\n")

while(1):
    details()
    enquiry()
    c=c+1
    print("VISITORS VISITED THIS SITE:",c)
    hour=(t.datetime.now().hour)
    minute=(t.datetime.now().minute)
    second=(t.datetime.now().second)
    if(hour==5) and (second==0) and (minute==0):
        print("DETAILS MAIL TO RESPECTIVE IDS")
        
