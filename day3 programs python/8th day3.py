test_list1 = []
test_list2 = []
 
# printing original lists
print ("The original list 1 is : " + str(test_list1))
print ("The original list 2 is : " + str(test_list2))
 
# using sorted()
# to combine two sorted lists
res = sorted(test_list1 + test_list2)
 
# printing result
print ("The combined sorted list is : " + str(res))
