import sys
def make_withdrawal(init_balance):
    init_balance = init_balance
    def wd(wd_amount):
        wd_amount = wd_amount
        # Checking whether balance is greater than withdrawal amount
        if init_balance < wd_amount:
            print("Your balance is too low for the withdrawal")
            return init_balance
        else:
            # Makes withdrawal
            new_balance = init_balance - wd_amount
            return new_balance
    return wd

print("The following code does not work because the inner function (wd()) does not update the balance after making a withdrawal. Instead, each time a withdrawal is made, it withdraws from the initial balance, without keeping track of the total amount withdrawn.")

wd = make_withdrawal(500)
balance1 = wd(72)
balance2 = wd(67)

print(balance1)
print(balance2)