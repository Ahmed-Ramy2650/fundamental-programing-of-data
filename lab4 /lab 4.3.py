x='yes'
while x=='yes' :
    for i in range(5):
        weight = float(input("Enter the weight: "))
        if weight < 0:
            print("Invalid weight. Please enter a non-negative weight.")
        else:
            unit = input("Enter weight unit (1 for mg, 2 for kg, 3 for ton): ")
            if unit == '1':
                converted_weight = weight / 1000
                print(f"{weight} mg is equal to {converted_weight} grams")
            elif unit == '2':
                converted_weight = weight * 1000
                print(f"{weight} Kg is equal to {converted_weight} grams")
            elif unit == '3':
                converted_weight = weight * 1000000
                print(f"{weight} Ton is equal to {converted_weight} grams")
            else:
                print("Invalid unit. PleaseEnter weight unit (1 for mg, 2 for kg, 3 for ton):")

        x = input("Do you want to continue? (yes/no): ").strip().lower()
        if x != "yes":
         break
print("Maximum number of attempts reached. Exiting the program.")
