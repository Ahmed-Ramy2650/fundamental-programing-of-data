friends = ['mark', 'william', 'majed', 'ropert', 'nader']
presents = ['car', 'playstation', 'football', 'basketball shoes']
x = input("What is in Joy's mind: ").strip().lower()
co=0
for i in presents:
    if x == i:
        co +=1
        index = presents.index(i)
        friend = friends[index]
        print("Oh ",friend," Thank you friend :)")
if co==0:
    print("Opps, Sorry none.")
