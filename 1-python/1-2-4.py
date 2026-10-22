
# Write a program to create a shopping list. 

# loop until "quit" is entered.
# input a grocery item
# input a quantity
# save the item as the key in the dictionary and quantity as the value
# if the item is in the dictionary already, add the quantity to the existing value


shopping_list = {}
while True:
    item = input("Enter a grocery item (or 'quit' to finish): ")
    if item.lower() == "quit":
        break
    quantity = int(input(f"Enter the quantity for {item}: "))
    
    if item in shopping_list:
        shopping_list[item] += quantity
    else:
        shopping_list[item] = quantity

print("Your shopping list:")
for item, quantity in shopping_list.items():
    print(f"- {item}: {quantity}")
    