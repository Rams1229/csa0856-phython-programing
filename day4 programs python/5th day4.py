a=input("enter a word: ")
def reverse(a):
    str = ""
    for i in a:
        str = i + str
    return str
 
print("The reversed string is : ", reverse(a))

    
    
