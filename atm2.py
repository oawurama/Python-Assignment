import sys
from datetime import date
class BankAccount:
    def __init__(self,balance):
        self.balance = balance 

    def pincheck(self):
        correct_pin = 1234
        pin = int(input("Please enter your pin: "))
        tries=1
        while correct_pin == 1234:
            if tries<3 and pin!= correct_pin:
                tries+=1
                pin=int(input("You have entered an incorrect pin. Please enter pin again:"))
                if tries == 3 and pin!= correct_pin:
                    print("Limit exceeded. Your card has been blocked. Please contact branch for more details!")
            else:
                if pin == correct_pin and tries <4:
                    print("Access granted")
                    if pin == correct_pin :
                        print ("Please proceed")    
                    correct_pin = False
            
    def withdraw(self):
        amount = int(input('Please enter amount to withdraw:'))
        withdrawal = 1
        keepAlive = True
        while keepAlive:
            #withdrawal+=1
            if amount < self.balance:
                self.balance -=amount
                #withdrawal+=1
                print('You have withdrawn GHs{}'.format (amount))
                print('You have Ghs{} left'.format (self.balance))
            elif amount >= self.balance:
                print  ("You do not have sufficient funds")
        
            else:
                while withdrawal < 3 and amount >= 2000:
                    self.balance -=amount
                    #withdrawal +=1
                    print ("You cannot withdraw more than GHS2000.00")
                    print('Please try again')
                    amount = False
            keepAlive = False

    def deposit (self):
        amount = int(input('Please enter amount to deposit:'))
        self.balance += amount
        print('You have deposited Ghs{}'.format (amount))
        print('You now have GHs{} in your account'.format (self.balance))
        
    def checkBalance (self):
        print ('Your current balance GHs{}'.format (self.balance))


def main():            
      print('WELCOME TO THE ATM')
      today = date.today()
      print ( today)
      bank = BankAccount(500)
      bank.pincheck()
      done=True
      while done==True:
            print(""" Please select what you would want to do
                  1. Withdraw
                  2. Deposit
                  3. Check Balance
                  4. Exit
                  """)
            choice=int(input("Enter Choice:"))
            if choice==1:
                        bank.withdraw()
            elif choice==2:
                        bank.deposit()
            elif choice==3:
                        bank.checkBalance()
            elif choice==4:
                  sys.exit()
                  
main()


        
        
