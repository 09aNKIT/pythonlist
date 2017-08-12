x=[0 ,1]
y=int(input("enter the range"))
for i in range(2,y):
    z=x[len(x)-1]+x[len(x)-2]
    x.append(z)
print x
