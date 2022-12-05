class Bank:
    def __init__(self,amount):
        self.amount = amount


    def Deposit(self,amount):
        self.amount += amount
    
    def Withdraw(self,amount):
        self.amount -= amount 
        
    def Balance(self):
        return self.amount

bank = Bank(0)

while True:
    print('Enter Your Choice:')
    print('1. Deposit\n2. Withdraw\n3. Balance\n4. Exit')
    choice = int(input())
    
    if choice == 1:
        print('Enter deposit amount:')
        Deposit = int(input())
        bank.Deposit(Deposit)
        
    elif choice == 2:
        print('Enter withdraw amount:')
        Deposit = int(input())
        bank.Deposit(Deposit)
        
    elif choice == 3:
        print('Display: Your current amount:')
        print(bank.Balance())
    elif choice == 4:
        break
