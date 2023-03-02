a=input("enter a word: ")
v='a','e','i','o','u'
c_vowels=0
for i in a:
    if(i in v):
        c_vowels+=1
print("count of vowels: ", c_vowels)
