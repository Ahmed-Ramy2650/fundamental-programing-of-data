department = ["Meat", "Seafood", "Milk", "Bread", "Oil"]
available = input("How many available items in the following departments? (Meat - Seafood - Milk - Bread - Oil): ").split()
prices = input("What are the prices of the available items in each department? ").split()

total = 0.0
cart = {dep: 0 for dep in department}
total_sold_items = 0

while True:
    quantity = input("How many you want from each department? (Meat - Seafood - Milk - Bread - Oil): ").split()
    for i in range(len(available)):
        if int(quantity[i]) <= int(available[i]):
            cart[department[i]] += int(quantity[i])
            available[i] = int(available[i]) - int(quantity[i])
            total_sold_items += int(quantity[i])
        elif int(quantity[i]) > int(available[i]):
            cart[department[i]] += int(available[i])
            available[i] = 0
        else:
            print(f"We are sorry, there's no available {department[i]}")

    promo_code = input("Please enter a promo if you have: ")
    if promo_code == "123456":
        if cart["Milk"] > 0:
            prices[2] = int(prices[2]) * 0.7

    for i in range(len(available)):
        total += int(prices[i]) * int(quantity[i])
    print(f"Dear prospective customer, the total is: {total} pounds")

    store_open = input("Is the store still open? (yes/no): ")
    if store_open.lower() != "yes":
        break
ratios = {dep: cart[dep] / total_sold_items for dep in department}

print("We sold today:")
while any(ratios.values()):
    max_ratio = 0
    max_department = ""
    for dep, ratio in ratios.items():
        if ratio > max_ratio:
            max_ratio = ratio
            max_department = dep
    if max_ratio > 0:
        print(f"{max_ratio * 100:.2f}% {max_department}")
        ratios[max_department] = 0
