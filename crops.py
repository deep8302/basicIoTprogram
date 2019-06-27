from tkinter import *
from tkinter import messagebox
import urllib.request
import webbrowser as wb
def kc():
    c=wb.open("https://en.wikipedia.org/wiki/Kharif_crop")
def rb():
    p=wb.open("https://en.wikipedia.org/wiki/Rabi_crop")
def zc():
    l=wbopen("https://en.wikipedia.org/wiki/Zaid_crops")
root=Tk()
root.title("calculator")
root.geometry('700x900')
root.configure(background="light blue")
f=Button(root,font=('arial',10,'bold'),text="kharif crop",width=40,command=kc)
f.place(x=10,y=120)
f=Button(root,font=('arial',10,'bold'),text="rabi crops",width=40,command=kc)
f.place(x=10,y=220)
f=Button(root,font=('arial',10,'bold'),text="Zaid crop",width=40,command=kc)
f.place(x=10,y=320)
root.mainloop()


