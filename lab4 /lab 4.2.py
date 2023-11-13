x = input("Soup: ")
y = input("Meal: ")

if (x == 'seafood' and (y == 'burger' or y == 'grilled chicken')):
    print("She hates vegetables")
elif ((x == 'vegetables' or x == 'mushroom') and y == 'mashed potatoes'):
    print("She loves vegetables")
else:
    print("She would neither hate nor love it")
