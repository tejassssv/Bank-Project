
def deposit(accounts, acc):
    print("       DEPOSIT      ")
    am = float(input("Enter amount to deposit: "))
    if am <=0:
        print("Amount must be greater than 0.")
        return

    accounts[acc]["Balance"] +=am
    accounts[acc]["History"].append( f"Credited: ₹{am:.2f}")
    print("Deposit successful!")
    print("New balance: ₹", accounts[acc]["Balance"])

def withdraw(accounts, acc):
    print("     WITHDRAW     ")
    am = float(input("Enter amount to withdraw: "))
    if am <= 0:
        print("Amount must be greater than 0.")
        return

    if am >accounts[acc]["Balance"]:
        print("Insufficient balance.")
        return
    accounts[acc]["Balance"] -=am
    accounts[acc]["History"].append(f"Debited: ₹{am:.2f}")
    print("Withdrawal successful!")
    print("New balance: ₹", accounts[acc]["Balance"])

def tra_his(accounts, acc):
    print("       TRANSACTION HISTORY  ")

    his = accounts[acc]["History"]
    if len(his) == 0:
        print("No transactions yet.")
        return
    for i, tran in enumerate(his, start=1):
        print(f"{i}. {tran}")