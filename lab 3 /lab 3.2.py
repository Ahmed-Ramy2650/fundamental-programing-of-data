x =input("Enter statment: ")
count = 0
for i in x:
    if i =='a' or i =='e' or i =='i' or i =='o' or i =='u':
        count = count + 1
if count >0:
    print("The number of vowels",count)
else:
    print("No vowels")
