test_str = 'this is a tree'
print("The original string is : " + str(test_str))
res = len([ele for ele in test_str if ele.isalpha()])
print("Count of Alphabets : " + str(res))
