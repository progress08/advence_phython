class BankAccount:
    def __init__(self, o, bal=0.0):
        self.__owner = o
        self.__balance = bal

    def deposit(self, amt):
        if amt > 0:
            self.__balance += amt
            print("Deposited $" + str(amt) + ". New balance: $" + str(self.__balance))
        else:
            print("Error: Deposit amount must be positive.")

    def withdraw(self, amt):
        if amt > 0:
            if amt <= self.__balance:
                self.__balance -= amt
                print("Withdrew $" + str(amt) + ". Remaining balance: $" + str(self.__balance))
            else:
                print("Error: Insufficient funds.")
        else:
            print("Error: Withdrawal amount must be positive.")

    def get_balance(self):
        return self.__balance
    
    def get_owner(self):
        return self.__owner

if __name__ == "__main__":
    acc = BankAccount("John Doe", 100)

    print("Account Owner: " + acc.get_owner())
    print("Initial Balance: $" + str(acc.get_balance()))

    print("\n--- Testing Deposit ---")
    acc.deposit(50)
    acc.deposit(-10)

    print("\n--- Testing Withdrawal ---")
    acc.withdraw(30)
    acc.withdraw(200)
    acc.withdraw(-20)

    print("\nFinal Balance: $" + str(acc.get_balance()))
    
    try:
        print(acc.__balance)
    except:
        print("\nconfirmed: Cannot access __balance directly.")
