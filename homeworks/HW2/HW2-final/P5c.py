def make_withdrawal(init_balance):
    init_balance = init_balance
    def wd(wd_amount):
        nonlocal init_balance
        wd_amount = wd_amount
        if init_balance < wd_amount:
            print("Your balance is too low for the withdrawal")
            return init_balance
        else:
            new_balance = init_balance - wd_amount
            init_balance = new_balance
            return init_balance
    return wd

wd = make_withdrawal(500)
balance1 = wd(40)
balance2 = wd(60)
balance3 = wd(65)

print(balance1)
print(balance2)
print(balance3)

# Must be run with Python3