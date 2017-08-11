import math
x=int(raw_input("enter the value"))
y=str(math.pi)
print len(y)
while x>len(y):
    print "no. is to large"
    x=int(raw_input("enter the no."))
else:
    print "%.*f" % (x,math.pi)
