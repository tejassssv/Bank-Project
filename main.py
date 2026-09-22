from account import accounts, create, login, details
from transactions import deposit, withdraw, tra_his

def user(acc):
    while True:
        print("       ACCOUNT MENU         ")
        print("Click 1 for Checking Balance of your Account")
        print("Click 2 for Depositing Money in the Bank")
        print("Click 3 for Withdrawing Money from the Bank")
        print("Click 4 for viewing Transaction History of your Account")
        print("Click 5 for showing Account Details")
        print("Click 6 for Logout")

        ch = int(input("Enter your choice: "))
        if ch == 1:
            print("      BALANCE    ")
            print("Current Balance: ₹", accounts[acc]["Balance"])
        elif ch== 2:
            deposit(accounts, acc)

        elif ch== 3:
            withdraw(accounts, acc)

        elif ch == 4:
            tra_his(accounts, acc)
        elif ch == 5:
            details(acc)

        elif ch== 6:
            print("  Logged out successfully.")
            break
        else:  print("Invalid choice. Please try again.")

def main():
    while True:
        print("       BANK MANAGEMENT SYSTEM      ")
        print("1. Open An Account")
        print("2. Login")
        print("3. Exit")

        c = int(input("Enter your choice: "))
        if c== 1:
            create()
        elif c== 2:
            ac = login()

            if ac is not None:
                user(ac)
        elif c == 3:
            print("Thank you")
            break
        else: print("Invalid choice, Please try again.")
if __name__ == "__main__":
    main()
