from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
        self.transaction_history = []
        self.interest_rate = 0.01

    def __str__(self):
        return f"account_number: {self.account_number}, balance: {self.balance}"

    @abstractmethod
    def can_withdrow(self, amount):
        pass

    def deposit(self, amount):
        self.balance += amount
        transaction = {"operation":"deposit", "amount":amount, "balance":self.balance}
        self.transaction_history.append(transaction)
        return transaction

    def withdraw(self, amount):
        if self.can_withdrow(amount):
            self.balance -= amount
            transaction = {"operation":"withdraw", "amount":amount, "balance":self.balance}
            self.transaction_history.append(transaction)
            return transaction
        else:
            return "You can't withdraw"

    def apply_interest(self):
        self.balance *= (1+self.interest_rate)
        transaction = {"operation":"withdraw", "amount":self.balance*0.05, "balance":self.balance}
        self.transaction_history.append(transaction)
        return transaction

    def get_transaction_history(self):
        result = f"----Transaction History----\n"
        for transaction in self.transaction_history:
            result += str(transaction) + "\n"
        return result

class SavingsAccount(Account):
    def can_withdrow(self, amount):
        if self.balance >= amount and amount < 10000:
            return True
        else:
            return False

class CheckingAccount(Account):
    def __init__(self, account_number, balance):
        super().__init__(account_number, balance)
        self.interest_rate = 0.05
    def can_withdrow(self, amount):
        if self.balance >= amount:
            return True
        else:
            return False
        
def process_deposit(account):
    if isinstance(account, Account):
        print(account.get_transaction_history())
    else:
        print("Cannot get transaction history")

if __name__ == "__main__":
    alice_savings = SavingsAccount("123456", 1000)
    bob_checking = CheckingAccount("987654", 500)

    accounts = [alice_savings, bob_checking]

    print("Initial Account Details:")
    print(alice_savings)
    print(bob_checking)

    print(alice_savings.deposit(200))
    print(alice_savings.withdraw(500))
    print(bob_checking.deposit(300))
    print(bob_checking.withdraw(1000))

    print(alice_savings.get_transaction_history())
    print(bob_checking.get_transaction_history())

    print(alice_savings)
    print(bob_checking)

    for account in accounts:
        process_deposit(account)