num =input("Enter list of integer number separated by space: ").split()
x =[int(i) for i in num]

print(sum(x))


print(sum(i for i in X if i%2!=0))


print(sum(1 for i in X if i>0))


print(any(i > 0 for i in X))
