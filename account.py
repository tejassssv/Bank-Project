accounts= {}
ac= 1000

def create():
    global ac
    print("         CREATE ACCOUNT     ")

    n = input("Enter your name: ")
    while True:
        pin = input("Create a 4-digit PIN: ")
        if len(pin) == 4 and pin.isdigit():
            break
        else:  print("PIN must contain exactly 4 digits.")

    while True:
        dp = float(input("Enter initial deposit: "))
        if dp >= 0:
            break
        else: print("Please enter a positive amount")
    ac += 1
    accounts[ac] = {
        "Name": n,
        "Pin": pin,
        "Balance": dp,
        "History": []
    }
    accounts[ac]["History"].append(f"Account created with initial deposit: ₹{dp:.2f}")

    print("Account created successfully!")
    print("Your account number is:", ac)
    return ac

def login():
    print("      LOGIN      ")

    acc = int(input("Enter account number: "))
    if not acc.isdigit():
        print("Enter valid account number")
        return None
    if acc not in accounts:
        print("Account not found")
        return None

    p = input("Enter PIN: ")
    if accounts[acc]["Pin"] == p:
        print("Login successful!")
        print("Welcome,", accounts[acc]["Name"])
        return acc
    else:
        print("Incorrect PIN.")
        return None

def details(ac):
    if ac not in accounts:
        print("Account not found")
        return
    a = accounts[ac]
    print("     ACCOUNT DETAILS      ")
    print("Account Number :", ac)
    print("Name           :", a["Name"])
    print("Balance        : ₹", a["Balance"])
