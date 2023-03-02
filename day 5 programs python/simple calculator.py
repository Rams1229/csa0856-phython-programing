x=int(input("x ="))
y=int(input("y ="))
print("1.add\n 2.sub\n 3.mul\n 4.div\n 5.pow\n")
z=int(input("enter your choice\n"))
def power(x, y):
 
    # initialize result by 1
    pow = 1
 
    # Multiply x for n times
    for i in range(y):
        pow = pow * x
 
    return pow
if(z == 1):
    print("x + y = ",x+y)
elif(z == 2):
    print("x - y = " ,x-y)
elif( z == 3):
    print("x*y =" ,x*y)
elif( z == 4):
    print("x/y =",x/y)
elif(z == 5):
    print("power = ",power(x,y))
else:
    print("enter valid choice")
