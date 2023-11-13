N = int(input("Enter the number="))
sum =0
if N<0:
    print("the number is negative")
else:
    for i in range(1,N+1,1):
        sum = sum + i
    print("summition of numbers=",sum)
