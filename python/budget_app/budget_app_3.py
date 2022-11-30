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

    def get_spent(self):
        spent = 0.0
        for transact in self.ledger:
            if transact.get('amount') < 0:
                spent += float(- transact.get('amount'))
        return spent

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
            filler = '*' * round((30-len(name))/2)
            title = filler + name + filler
            return title + '\n'
        title = makeTitle(self.name)
        
        transactions = ''
        for transact in self.ledger:
            desc = transact.get('description')[0:23]
            amt = format(transact.get('amount'),'.2f') # float function returns a string
            if len(amt) > 7:
                amt = amt[0:7]

            filler = ' ' * round(30-len(desc)-len(amt))
            transactions +=  desc + filler + amt + '\n'
        
        total = f'Total: {round(self.get_balance(),2)}'

        return title + transactions + total


def create_spend_chart(categories):
    chart = 'Percentage spent by category\n'
    # Names
    names = [catgr.name for catgr in categories]

    # Creating percentage
    spent = [catgr.get_spent() for catgr in categories]
    spent_total = sum(spent)
    category_percentage  = []
    for s in spent:
        perc = s / spent_total * 100
        perc = perc // 10 * 10
        category_percentage.append(int(perc))
    # print(category_percentage)

    # Creating percentage chart 
    for num in range(100,0-1,-10):
        num = str(num) 
        line = ' ' * (3-len(num)) + num + '|'
        for indx, cat_perc in  enumerate(category_percentage):
            indx += 1
            
            if int(num) > cat_perc:
                line += ' ' * 3
                continue
            line += f' o '

        chart += line + ' \n'

    chart += ' ' * 4 + '-' * (len(categories) * 3 + 1)

     # Define a function to pivot text from horizontal to vertical
    def pivot_txt(texts, lmargin = 0):
      """ Receive list of strings
      Display the strings vertically
      Each string is seperatred with a space
      Returns display
      """
      string_out = ''
      string_max_length = max(len(t) for t in texts)
      # line_list = []
      for i in range(string_max_length):
          string_out += ' ' * lmargin
          for t in texts:
              try: 
                  letter = t[i]
                  string_out += f' {letter} ' 
              except:
                  string_out += ' ' * 3
                  continue
          if i != (string_max_length - 1): 
              string_out += f' \n'
          else:
              string_out += ' '

      return string_out
    
    # Creating name chart
    chart += '\n' + pivot_txt(names,lmargin = 4)    
    return chart
