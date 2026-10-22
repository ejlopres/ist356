'''
Let's write a program to divide up the check among diners in a party.
Write a program to input the amount of a restaurant check, tip %, and number of diners
The program should output the total amount with tip, and the amount each diner owes.
'''

check_amount = float(input("Enter the amount of the restaurant check: "))
tip_percentage = float(input("Enter the tip percentage: "))
number_of_diners = int(input("Enter the number of diners: "))

if check_amount < 0 or tip_percentage < 0 or number_of_diners < 0:
	print("Error: inputs cannot be below zero.")
elif number_of_diners == 0:
	print("Error: the number of diners must be above zero.")
else:
	total_with_tip = check_amount + (check_amount * tip_percentage / 100)
	amount_per_diner = total_with_tip / number_of_diners

	print(f"Total amount with tip: ${total_with_tip:.2f}")
	print(f"Amount each diner owes: ${amount_per_diner:.2f}")

