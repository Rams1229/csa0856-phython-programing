print("Enter Two Numbers: ", end="")
n = int(input())
m = int(input())

a = n
b = m
while b!=0:
    temp = b
    b = a%b
    a = temp

gcd = a
lcm = int((n*m)/gcd)

print("\nLCM  = ", lcm)
print("gcd = ", gcd)
