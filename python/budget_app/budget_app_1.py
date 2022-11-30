class Category:
    def __init__(self,name):
        self.name = name
        self.ledger = []
        
    def get_balance(self):
        """Returns current balance of budget category
        """
        self.balance = 0
        for transact in self.ledger:
            self.balance += transact.get('amount',0)

        return float(self.balance)

    def deposit(self, amount,description = ""):
        """ Accepts amount and description
        Description is empty string by default
        Append an object to the ledget list in form of:
        {"amount": amount, "description": description}
        """
        self.ledger.append(
            {
                'amount': float(amount),
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
        """Accepts amount and description
        Description is empty string by default
        Append an object to the ledget list in negative value of amount:
        {"amount": -amount, "description": description}
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

    def __str__(self):
        """ Object should be printed with style
        * A title line of 30 characters
        where the name of the category is centered in a line of * characters.

        * A list of the items in the ledger.
        Each line should show the description and amount.
        
        * A line displaying the category total.
        """
        def makeTitle(name):
            title = ''
            place_holder = '*' * round((30-len(name))/2)
            title = place_holder + name + place_holder
            return title + '\n'
        title = makeTitle(self.name)
        
        transactions = ''
        for transact in self.ledger:
            desc = transact.get('description')[0:23]
            amt = format(transact.get('amount'),'.2f') # float function returns a string
            if len(amt) > 7:
                amt = amt[0:7]

            place_holder = ' ' * round(30-len(desc)-len(amt))
            transactions +=  desc + place_holder + amt + '\n'
        
        total = f'Total: {round(self.get_balance(),2)}'

        return title + transactions + total
