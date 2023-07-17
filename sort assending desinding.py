ab=[]
n=int(input("Enter Range: "))
for a in range (0,n):
    x=int(input("x: "))
    ab.append(x)
print(ab)
ab.sort()

print("Ascending order",ab)
n=ab[::-1]
print("Desending order",n)
