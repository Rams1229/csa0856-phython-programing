def maxArea(A, Len) :
    area = 0
    for i in range(Len) :
        for j in range(i + 1, Len) :
            area = max(area, min(A[j], A[i]) * (j - i))
    return area
a =int(input("enter the number of elements:"))
if(a>0):
    b=[]
    for i in range(0,a):
        c=int(input("enter the number: "))
        b.append(c)
print("input array=",b)
print("output=",maxArea(b,a))
