lst = [1,2,1,2,3,4,]
fre = {}

for item in lst:
   if item in fre:
      fre[item] += 1
   else:
      fre[item] = 1

print(fre)
