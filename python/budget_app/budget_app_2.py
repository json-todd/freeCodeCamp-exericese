
def create_spend_chart(categories):
    chart = 'Percentage spent by category\n'
    
    # Creating percentage
    spent = [catgr.get_spent() for catgr in categories]
    spent_total = sum(spent)
    category_percentage  = []
    for s in spent:
        perc = s / spent_total * 100
        perc = perc // 10 * 10
        category_percentage.append(int(perc))
    print(category_percentage)

    # Creating lines
    for num in range(100,0-1,-10):
        num = str(num) 
        line = ' ' * (3-len(num)) + num + '|'
        
        chart += line
    
    # Return chart
    chart += ' ' * 4 + '-' * (len(categores) * 2 + 2)
    return chart
