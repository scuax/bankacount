class BankAccount:
    def __init__(self, account_number):
        self.account_number=account_number
        self.balance=0
    def deposit(self,amount):
        if amount > 0:
            self.balance+=amount
            print("Depositaste" ,amount," Saldo actual:",self.balance)
        else:
            print("El monto de depósito debe ser positivo.")
    def withdraw(self,amount):
        if amount >0 and amount<=self.balance:
            self.balance-=amount
            print("Retiraste" ,amount, "Saldo actual:" ,self.balance)
        elif amount>self.balance:
            print("Fondos insuficientes.")
        else:
            print("El monto de retiro debe ser positivo.")
    def get_balance(self):
        return (self.balance)
    def __str__(self):
        return "Número de Cuenta: ",self.account_number,", Saldo:",self.balance