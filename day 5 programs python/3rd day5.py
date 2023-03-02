a=input("enter the grade of the employee: ")
b=int(input("enter the salary : "))
print("salary= ",b)
if( a == 'A'):
    bonus= (5/100)*b
    f.s= bouns + b
    print("bouns = ",bonus)
    print("total to be paid = ",f.s)
elif( a == 'B'):
    bo = (10/100)*b
    s = bo + b
    print("bouns = ",bo)
    print("total to be paid = ",s)
elif( b < 10000 and a == 'A'):
    bon = (5/100)*b + (2/100)*b
    sa = bon + b
    print("bouns = ",bon)
    print("total to be paid = ",sa)
elif( b < 10000 and a == 'B'):
    bonu = (10/100)*b + (2/100)*b
    sal = bonu + b
    print("bouns = ",bonu)
    print("total to be paid = ",sal)
else:
    print("invalid input")
    
