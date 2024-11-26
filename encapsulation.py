class BankAccount:
    def __init__(self,account_number,balance):
        self.__account_number=account_number
        self.__balance = balance
    def deposite(self,amount):
        self.__balance += amount
        print(f"Deposited{amount}.New balance is {self.__balance}.")
    def withdraw(self,amount):
        if amount<=self.__balance:
            self.__balance -= amount
            print(f"withdraw{amount}.new balance is {self.__balance}.")
        else:
            print("Insufficient balance.")
account=BankAccount("1234567",1000)
account.deposite(500)
account.withdraw(200)
                    
            