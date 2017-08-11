a,b = 0,1
n=int(raw_input("enter the range"))
print a
print b
for i in range(2,n):
    c=a+b
    a=b
    b=c
    print c
