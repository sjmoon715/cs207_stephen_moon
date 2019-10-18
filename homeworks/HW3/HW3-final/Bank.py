from enum import Enum
class AccountType(Enum):
    SAVINGS = 1
    CHECKING = 2
class BankAccount():
    def __init__(self, owner, accountType):
        self.owner = owner
        self.accountType = accountType
        self.balance = 0

    # Withdrawal Method with ValueError exception if amount is too large or less than 0
    def withdraw(self, amount):
        self.amount = amount
        if amount > self.balance or amount < 0:
            raise ValueError("Invalid Withdrawal Amount")
        else:
            self.balance = self.balance - amount
            return self.balance

    # Deposit Method with ValueError exception if amount less than 0
    def deposit(self, amount):
        self.amount = amount
        if amount < 0:
            raise ValueError("Invalid Deposit Amount")
        else:
            self.balance = self.balance + amount
            return self.balance
    # __str__ method for info on account
    def __str__(self):
        accountType = self.accountType
        return "Account Owner: " +self.owner+ "\nAccount Type: " +self.accountType.name
    # returns balance of account
    def __len__(self):
        return self.balance

class BankUser():
    def __init__(self, owner):
        self.owner = owner
        self.checking_account = None
        self.savings_account = None
    # addAccount methods adds either checking or savings
    def addAccount(self, accountType):
        if accountType == AccountType.CHECKING:
            if self.checking_account == None:
                self.checking_account = BankAccount(self.owner, accountType)
                # Initializes balance of new account at 0
                self.checking_account.balance = 0
                return self.checking_account
            else:
                raise ValueError("You already have a checking account")
        if accountType == AccountType.SAVINGS:
            if self.savings_account == None:
                self.savings_account = BankAccount(self.owner, accountType)
                # Initializes balance of new account at 0
                self.savings_account.balance = 0
                return self.savings_account
            else:
                raise ValueError("You already have a savings account")
    # getBalance returns balance given account type            
    def getBalance(self, accountType):
        if accountType == AccountType.SAVINGS:
            # Checks whether account exists
            if self.savings_account == None:
                raise ValueError("You don't have a savings account")
            else:
                return self.savings_account.balance
        if accountType == AccountType.CHECKING:
            # Checks whether account exists
            if self.checking_account == None:
                raise ValueError("You don't have a checking account")
            else:
                return self.checking_account.balance
    # Deposit method
    def deposit(self, accountType, amount):
        self.amount = amount
        if accountType == AccountType.SAVINGS:
            # Checks whether account exists
            if self.savings_account == None:
                raise ValueError("You don't have a savings account")
            else:
                if amount < 0:
                    raise ValueError("Invalid Deposit Amount")
                else:
                    # Updates balance
                    self.savings_account.balance = self.savings_account.balance + amount
                    return self.savings_account.balance
        if accountType == AccountType.CHECKING:
            # Checks whether account exists
            if self.checking_account == None:
                raise ValueError("You don't have a checking account")
            else:
                if amount < 0:
                    raise ValueError("Invalid Deposit Amount")
                else:
                    # Updates balance
                    self.checking_account.balance = self.checking_account.balance + amount
                    return self.checking_account.balance
    # Withdrawal Method
    def withdraw(self, accountType, amount):
        self.amount = amount
        if accountType == AccountType.SAVINGS:
            # Checks whether account exists
            if self.savings_account == None:
                raise ValueError("You don't have a savings account")
            else:
                if amount > self.savings_account.balance or amount < 0:
                    raise ValueError("Invalid Withdrawal Amount")
                else:
                    # Updates Balance
                    self.savings_account.balance = self.savings_account.balance - amount
                    return self.savings_account.balance
        if accountType == AccountType.CHECKING:
            # Checks whether account exists
            if self.checking_account == None:
                raise ValueError("You don't have a checking account")
            else:
                if amount > self.checking_account.balance or amount < 0:
                    raise ValueError("Invalid Withdrawal Amount")
                else: 
                    # Updates Balance   
                    self.checking_account.balance = self.checking_account.balance - amount
                    return self.checking_account.balance

    # __str__ method for info on account
    def __str__(self):
        if self.checking_account == None and self.savings_account == None:
            number_of_accounts = 0
            return "Number of Accounts: "+str(number_of_accounts)
        elif self.checking_account != None and self.savings_account != None:
            number_of_accounts = 2
            return "Number of Accounts: "+str(number_of_accounts)+"\nChecking Account Balance: $"+str(self.checking_account.balance)+"\nSavings Account Balance: $"+str(self.savings_account.balance)
        else:
            number_of_accounts = 1
            if self.checking_account == None: 
                return "Number of Accounts: "+str(number_of_accounts)+"\nSavings Account Balance: $"+str(self.savings_account.balance)
            else:
                return "Number of Accounts: "+str(number_of_accounts)+"\nChecking Account Balance: $"+str(self.checking_account.balance)

def ATMSession(bankUser):
    bankUser = BankUser(bankUser)
    def interface():
        # Creating 1st set of menu options
        menu = {}
        menu['1']="1) Exit"
        menu['2']="2) Create Account"
        menu['3']="3) Check Balance"
        menu['4']="4) Deposit"
        menu['5']="5) Withdraw"
        options = menu.keys()
        
        # Creating 2nd set of menu options
        menu2 = {}
        menu2['1'] = "1) Checking"
        menu2['2'] = "2) Savings"
        options2 = menu2.keys()

        # Prints 1st menu until loop = False
        loop = True
        while loop:
            for entry in options:
                print (menu[entry])
            selection = input("Enter Option: ")
            # Ends loop if user picks exit
            if selection == '1':
                loop = False
            # Create Account Option
            elif selection == '2':
                loop2 = True
                # Prompts user for account type
                while loop2:
                    # Prints 2nd menu options
                    for entry in options2:
                        print (menu2[entry])
                    # Takes user input
                    selection2 = input("Enter Option: ")
                    if selection2 == '1':
                        try:
                            bankUser.addAccount(AccountType.CHECKING)
                            print("Checking account created!")
                            loop2 = False
                        except ValueError as v:
                            print(v)
                            loop2 = False
                    elif selection2 == '2':
                        try:
                            bankUser.addAccount(AccountType.SAVINGS)
                            print("Savings account created!")
                            loop2 = False
                        except ValueError as v:
                            print(v)
                            loop2 = False
                    else:
                        print("Invalid option selected.")
            # Check Balance Option
            elif selection == '3':
                loop2 = True
                # Prompts user for account type
                while loop2:
                    for entry in options2:
                        print (menu2[entry])
                    selection2 = input("Enter Option: ")
                    # Takes user input
                    if selection2 == '1':
                        try:
                            bankUser.getBalance(AccountType.CHECKING)
                            print("Current balance: $"+str(bankUser.checking_account.balance))
                            loop2 = False
                        except ValueError as v:
                            print(v)
                            loop2 = False
                    elif selection2 == '2':
                        try:
                            bankUser.getBalance(AccountType.SAVINGS)
                            print("Current balance: $"+str(bankUser.savings_account.balance))
                            loop2 = False
                        except ValueError as v:
                            print(v)
                            loop2 = False
                    else:
                        print("Invalid option selected.")
            # Deposit Option
            elif selection == '4':
                print("Deposit")
                loop2 = True
                # Prompts user for account type
                while loop2:
                    for entry in options2:
                        print (menu2[entry])
                    selection2 = input("Enter Option: ")
                    # Takes user input
                    if selection2 == '1':
                        try:
                            amount = int(input("Enter an integer amount, cannot be negative: "))
                            bankUser.deposit(AccountType.CHECKING, amount)
                            print("Current balance: $"+str(bankUser.checking_account.balance))
                            loop2 = False
                        # Handles invalid amounts and returns user to 1st menu
                        except ValueError as v:
                            print(v)
                            loop2 = False
                    elif selection2 == '2':
                        try:
                            amount = int(input("Enter an integer amount, cannot be negative: "))
                            bankUser.deposit(AccountType.SAVINGS, amount)
                            print("Current balance: $"+str(bankUser.savings_account.balance))
                            loop2 = False
                        # Handles invalid amounts and returns user to 1st menu
                        except ValueError as v:
                            print(v)
                            loop2 = False
                    else:
                        print("Invalid option selected.")
            # Withdrawal Option
            elif selection == '5':
                print("Withdrawal")
                loop2 = True
                while loop2:
                    for entry in options2:
                        print (menu2[entry])
                    selection2 = input("Enter Option: ")
                    # Takes user input
                    if selection2 == '1':
                        try:
                            amount = int(input("Enter an integer amount, cannot be negative: "))
                            bankUser.withdraw(AccountType.CHECKING, amount)
                            print("Current balance: $"+str(bankUser.checking_account.balance))
                            loop2 = False
                        # Handles invalid amounts and returns user to 1st menu
                        except ValueError as v:
                            print(v)
                            loop2 = False
                    elif selection2 == '2':
                        try:
                            amount = int(input("Enter an integer amount, cannot be negative: "))
                            bankUser.withdraw(AccountType.SAVINGS, amount)
                            print("Current balance: $"+str(bankUser.savings_account.balance))
                            loop2 = False
                        # Handles invalid amounts and returns user to 1st menu
                        except ValueError as v:
                            print(v)
                            loop2 = False
                    else:
                        print("Invalid option selected.")
            else:
                print("Invalid Option Selected")

    return interface()

