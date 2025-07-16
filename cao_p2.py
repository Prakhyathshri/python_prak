class Account:

    def __init__(self, balance, account_no):
        self.balance = balance
        self.account_no = account_no
    
    def debit(self, amount):
        self.balance -= amount
        print("RS",amount,"was debited from your account number",self.account_no,"and balance is",self.balance)
    
    def credit(self,amount):
        self.balance += amount
        print("RS",amount,"was debited from your account number",self.account_no,"and balance is",self.balance)
            
    def get_balance(self):
        print("Your final balance is",self.balance)

acc1 = Account(10000,12345)
acc1.debit(1000)
acc1.credit(500)
acc1.get_balance()