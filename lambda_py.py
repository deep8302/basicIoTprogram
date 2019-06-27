import functools as ft
l=[1,2,3,4,5,6,7,8,9,10]
g2=[]
g=list((map(lambda x:x*x,l)))
print(g)
g1=list(filter(lambda x:x%2==0,map(lambda x:x*x,l)))
print(g1)
g2=lambda z,y:z*y
g2=list(ft.reduce(g2,g1))#(filter(lambda x:x%2==0,map(lambda x:x*x,l)))))
print(g2)
g2=lambda x,y:x*y
#print(g2(g1[1]))
