# Bank-Project
Its a simple prototype of bank containing 3 modules(main, accounts, transactions) made by using basic python, this banking application that is lightweight and operates from a terminal.

## Features
When registering an account, the system provides an interactive option for setting it up, including verification of a 4-digit security PIN and an initial deposit.
Secure Login: Access to personal banking actions is given only after the user has been authenticated using their account number and PIN.
You can deposit or withdraw money instantly, with automatic input validation to stop negative amounts or overdrafts.
Transaction History: It maintains a record of all the account activities, including the timestamps or descriptions of the actions (such as an Initial Deposit, Debits, and Credits).
Overview of Account Details:This allows you to view the account holder's profile details and check the current balance.

## Module Breakdown

main.py: This is the entry point for the application and is responsible for displaying the main menu interface as well as directing the user's to different options
account.py: Contains the logic for creating accounts, handles user credentials, verifies logins, and displays the profile details.
transactions.py: Contains the logic for handling deposits, withdrawals, and for tracking transaction history.

### Running the Application

1. Get a copy of this project repository or download it.
2. Access the terminal or command prompt and go to the project directory.
3. Run the main script.

```bash
python main.py
```

**Instructions for Testing**

To thoroughly test the application, try the following scenarios:

Create an account: Start the app, choose the option to create an account, enter a name, and set a PIN. Note down the generated account number.

Test validation: Try logging in with a fake account number or wrong PIN. The system should deny access.

Test transactions: Log in successfully and try to deposit 500. Check the balance. Then try to withdraw 1000 (more than your balance) to ensure the insufficient funds warning pops up. Finally, withdraw a valid amount and check the balance again.

Exit: Use the logout/exit options to ensure the program closes cleanly.
