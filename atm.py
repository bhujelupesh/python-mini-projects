amount = 1000

while True:
    print("1. Balance Check")
    print("2. Deposit Amount")
    print("3. Withdraw Money")
    print("4. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        print(f"Current Balance : {amount}")
    elif choice == '2':
        deposit = int(input("Enter the amount to be deposited: "))
        amount += deposit
        print(f"Successfully deposited")
    elif choice == '3':
        withdraw = int(input("Enter the amount to be withdrawn: "))
        if amount < withdraw:
            print("Insufficient balance")
        else:
            amount -= withdraw
            print(f"Remaining Balance : {amount}")
    elif choice == '4':
        print("Thank you for using our sevice")
        break
    else:
        print("Invalid choice")