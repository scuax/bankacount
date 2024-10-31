from classbank import BankAccount
account = BankAccount("123456789")

while True:
    print("\n¿Qué transacción quieres realizar?")
    print("1 para Depositar")
    print("2 para Retirar")
    print("3 para Consultar Saldo")
    print("4 para Salir")

    choice = input("Selecciona una opción (1-4): ")
    if choice=="1":
        amount=float(input("¿Cuánto deseas depositar? "))
        account.deposit(amount)
    elif choice=="2":
        amount=float(input("¿Cuánto deseas retirar? "))
        account.withdraw(amount)
    elif choice=="3":
        print("Saldo actual:",account.get_balance)
    elif choice=="4":
        print("Gracias por usar el sistema bancario.")
        break
    else:
        print("Opción no válida, por favor elige de nuevo.")
    