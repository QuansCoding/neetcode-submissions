class Account:
    def __init__(self,title,balance):
        self.title = title
        self.balance = balance
        pass
    
    def display_balance(self) -> None:
        print(f"Balance: ${self.balance}")
        pass


# Do not modify the code below this line
account = Account("John", 1000)
account.display_balance()
