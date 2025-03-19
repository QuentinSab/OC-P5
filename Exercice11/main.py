# Écrivez votre code ici !
class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Impossible de déposer un montant négatif d'argent.")
        else:
            self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Le solde du compte n'est pas suffisant.")
        else:
            self.balance -= amount

    def display_balance(self):
        print(f"Le propriétaire du compte est {self.account_holder}.")
        print(f"Son solde est de {self.balance} €.")
