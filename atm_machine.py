# ============================================================
# PF Python - Project: ATM Machine Simulator
# ============================================================

pin = "1234"
balance = 1000

enter_pin = input("Enter PIN: ")

if pin == enter_pin:
    print("PIN correct. Welcome!")

    while True:
        print("\n--- ATM MENU ---")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            print(f"Your balance is Rs.{balance}")

        elif choice == 2:
            amount = int(input("Enter amount to deposit: Rs."))
            balance += amount
            print(f"Deposited Rs.{amount}. New balance: Rs.{balance}")

        elif choice == 3:
            amount = int(input("Enter amount to withdraw: Rs."))
            if amount <= balance:
                balance -= amount
                print(f"Withdrawn Rs.{amount}. New balance: Rs.{balance}")
            else:
                print("Insufficient balance.")

        elif choice == 4:
            print("Thank you. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")
else:
    print("Wrong PIN. Access denied.")
