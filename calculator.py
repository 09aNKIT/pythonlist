def add(x ,y):
    return(x+y)
def sub(x ,y):
    return(x-y)
def multiply(x ,y):
    return(x*y)
def divide(x ,y):
    return(x /y)
print "1:addition"
print "2:substraction"
print "3:multiplication"
print "division"
choice= input("enter choice")
x=int(input("enter 1st no."))
y=int(input("enter 2nd no"))
if choice ==1:
    print add(x,y)
elif choice==2:
    print sub(x,y)
elif choice ==3:
    print multiply(x,y)
elif choice ==4:
    print divide(x,y)
else:
    print "wrong choice"
