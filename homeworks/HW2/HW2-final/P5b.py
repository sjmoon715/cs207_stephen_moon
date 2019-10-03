import sys
def make_withdrawal(init_balance):
    init_balance = init_balance
    def wd(wd_amount):
        wd_amount = wd_amount
        if init_balance < wd_amount:
            print("Your balance is too low for the withdrawal")
            return init_balance
        else:
            new_balance = init_balance - wd_amount
            init_balance = new_balance
            return init_balance
    return wd

print("The name 'init_balance' has not been bound to anything within the inner function wd(), so Python does not recognize what it is referring to.")

wd = make_withdrawal(500)
balance1 = wd(42)
balance2 = wd(68)

print(balance1)
print(balance2)