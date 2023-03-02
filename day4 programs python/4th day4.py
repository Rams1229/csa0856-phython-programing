n=int(input("enter total no.of users: "))
m=int(input("enter the staff users: "))
a= (n-m)-(m/3)
if( n>=0 and m>=0):
    print("student user : " , a)
else:
    print("invalid input")
