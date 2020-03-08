
correct_pin = 1234
print("Welcome to the ATM")
pin = int(input("Please enter your pin: "))
tries=1
balance=10000
withdrawals = 1
while correct_pin == 1234:
    if tries<3 and pin!= correct_pin:
        tries+=1
        pin=int(input("You have entered an incorrect pin. Please enter pin again:"))
        if tries == 3 and pin!= correct_pin:
            print("Limit exceeded. Your card has been blocked. Please contact branch for more details!")

    else:
        if pin == correct_pin and tries <4:
            print("Welcome")
            print("You have 10,000 in your account")
            if pin == correct_pin and withdrawals <3:
                withdrawals+=1
                cash=int(input("Please enter amount to withdraw:"))
                print ("Please take cash")
                print("Your cash balance is {}".format(balance-cash))
                print ("Thank you for banking with us!")
            else:
                print('You have exceeded your withdrawal limit')
            correct_pin = False
