from Bank import *

# For BankAccount Class
def BA_test_over_withdrawal():
    try:
        steve = BankAccount("Stephen", AccountType.SAVINGS)
        steve.deposit(40)
        steve.withdraw(50)
    except ValueError as v:
        print(v)
def BA_negative_deposit():
    try:
        steve = BankAccount("Stephen", AccountType.SAVINGS)
        steve.deposit(-40)
    except ValueError as v:
        print(v)
def BA_negative_withdrawal():
    try:
        steve = BankAccount("Stephen", AccountType.SAVINGS)
        steve.withdraw(-40)
    except ValueError as v:
        print(v)

# For BankUser Class
def BU_test_over_withdrawal():
    stephen = BankUser("Stephen")  
    stephen.addAccount(AccountType.SAVINGS)  
    stephen.addAccount(AccountType.CHECKING)  
    stephen.deposit(AccountType.SAVINGS, 300)
    stephen.deposit(AccountType.CHECKING, 450)
    try:
        # Valid withdrawal amount  
        stephen.withdraw(AccountType.SAVINGS, 275)
        # Withdrawal amount too high
        stephen.withdraw(AccountType.CHECKING, 455)
    except ValueError as v:
        print(v)
def BU_test_negative_deposit():
    stephen = BankUser("Stephen")  
    stephen.addAccount(AccountType.SAVINGS)    
    try:   
        # Negative deposit amount
        stephen.deposit(AccountType.SAVINGS, -215)
    except ValueError as v:
        print(v)
def BU_test_negative_withdrawal():
    stephen = BankUser("Stephen")  
    stephen.addAccount(AccountType.SAVINGS)    
    try:   
        # Negative withdrawal amount
        stephen.withdraw(AccountType.SAVINGS, -215)
    except ValueError as v:
        print(v)
def BU_accountType_none():
    stephen = BankUser("Stephen")   
    try:   
        stephen.deposit(AccountType.CHECKING, 215)
    except ValueError as v:
        print(v)
def BU_double_account():
    stephen = BankUser("Stephen")  
    stephen.addAccount(AccountType.SAVINGS)    
    stephen.deposit(AccountType.SAVINGS, 300)
    try:   
        stephen.addAccount(AccountType.SAVINGS)
    except ValueError as v:
        print(v)

# BankAccount Tests
print("BankAccount Tests:")
BA_test_over_withdrawal()
BA_negative_deposit()
BA_negative_withdrawal()


# BankUser Tests
print("\nBankUser Tests:")
BU_test_over_withdrawal()
BU_test_negative_deposit()
BU_test_negative_withdrawal()
BU_accountType_none()
BU_double_account()