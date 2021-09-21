class Category:
    def __init__(self,name):
        self.name = name
        self.ledger = []
        
    def get_balance(self):
        self.balance = 0
        for transact in self.ledger:
            self.balance += transact.get('amount',0)

        return float(self.balance)

    def deposit(self, amount,description = ""):
        """
        """
        self.ledger.append(
            {
                'amount': amount,
                'description': description
            }
        )

    def check_funds(self,amount):
        """ Accepts an amount as argument
        Returns `False` if amount > balance
        or `True` otherwise
        """
        balance = self.get_balance()
        if amount > balance: return False
        else: return True

    def withdraw(self, amount, desciption = ""):
        """
        """
        if self.check_funds(amount):
        
            self.ledger.append(
                {
                    'amount': float(-amount),
                    'description': desciption
                }
            )

            return True
        
        else:
            return False

    def transfer(self, amount, other):
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {other.name}')
            other.deposit(amount, f'Transfer from {self.name}')
            return True

        else:
            return False
