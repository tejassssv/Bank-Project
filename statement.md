Problem Statement

Managing personal finances often starts with understanding the basic flow of banking—deposits, withdrawals, and account security. While modern banks use complex graphical apps and databases, understanding the core logic behind these systems can be overwhelming for beginners. There is a need for a simplified, educational simulation that demonstrates how backend banking algorithms operate without the distraction of a complex UI.

Scope of the Project

This project focuses on the core functional logic of a banking system.
In-Scope:

Creating new user accounts with basic details.

Implementing a rudimentary authentication system (Account Number + PIN).

Processing basic math operations for deposits and withdrawals.

Navigating via a text-based console menu.

Out-of-Scope:

Persistent database storage (e.g., SQL).

Advanced encryption for data over a network.

Inter-bank or peer-to-peer money transfers.

Graphical User Interface (GUI).

Target Users

Programming Students: Those looking to understand how modular programming (splitting code into different files) and basic state management work in Python.

General Users: People interested in a quick, local, sandbox environment to see how a basic ledger calculates transactions.

High-Level Features

Modular Architecture: Logic is divided into distinct files for user interface (main.py), account handling (account.py), and money management (transactions.py).

Session Security: Users are required to authenticate before accessing any sensitive transaction menus.

Dynamic Validation: The system actively checks for invalid inputs, such as negative deposit amounts or withdrawals that exceed the current balance, preventing mathematical errors.
