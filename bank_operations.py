# BANK OPERATIONS 
class Bank:
    bankname = "Indian Oversees Bank"
    branch   = "A23,BBSR,Indian"

    # CREATE NEW ACCOUNT
    def __init__(self,username,pan,address):
        self.username = username 
        self.pan      = pan 
        self.address  = address 
        self.balance  = 0.0
        print(f"Hello, {self.username} cong! your account created successfully") 

    # DEPOSIT 
    def deposit(self,amount):
        self.balance = self.balance + amount
        print(f"{amount} deposited successfully")

    # WITHDRAW 
    def withdraw(self,amount):
        if self.balance > amount:
            self.balance = self.balance - amount 
            print(f"{amount} withdraw successfully")
        else:
            print(f"you have insufficent balance")
    # BALANCE CHECK
    def check_balance(self):
        print(f"{self.balance} Your available bank balance")

# CREATE BANK INSTANCE 
username = input('enter your name: ')
pan      = input('pan: ')
address  = input('address: ')

B = Bank(username,pan,address)


# OPERATION MANAGEMENT 
while True:
    print('Please Select Any Options: ')
    print('1.Deposit\n2.Withdraw\n3.Ministatement\n4.Stop')
    option = int(input(''))



        # # MENU OPTIONS
        # actions = {
        #     1: lambda: bank.deposit(int(input('Enter the amount to deposit: '))),
        #     2: lambda: bank.withdraw(int(input('Enter the amount to withdraw: '))),
        #     3: lambda: bank.check_balance(),
        #     4: exit
        # }



    # ACTIONS 
    if option       == 1:
        amount      = int(input('please enter your amount: '))
        B.deposit(amount)
    elif option     == 2:
        amount      = int(input('please enter your amount: '))
        B.withdraw(amount)
    elif option     ==3:
        B.check_balance()
    else:
        break 


