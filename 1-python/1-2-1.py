PASSWORD = "secret"


for attempt in range(5):
    entered_password = input("Enter the password: ")    

    if PASSWORD == entered_password:
        print("Access granted") 
        break
    else:
        print("Access denied")

    print(f"You have {4 - attempt} attempts left.")

else: print("You are locked out of the system. Please contact the administrator.")