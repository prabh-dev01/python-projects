import math

class Category:
    def __init__(self,name):
        self.name=name
        self.ledger=[]

    def deposit(self,amount,description=''):
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self,amount,description=''):
        
        if self.check_funds(amount):
                self.ledger.append({'amount': -amount, 'description': description})
                return True
        return False    


    def check_funds(self,amount):
        
        if amount>self.get_balance():
            return False
        return True    

    def get_balance(self):
        return sum(i["amount"] for i in self.ledger)

    def transfer(self,amount,destination):
        if self.check_funds(amount):

           self.withdraw(amount,f"Transfer to {destination.name}")
           destination.deposit(amount,f"Transfer from {self.name}")
           return True
        return False   
           

       



    def __str__(self):

        result = self.name.center(30, '*') + '\n'
        for item in self.ledger:


            description = item['description']
            amount = item['amount']
            result += description[:23].ljust(23) + f'{amount:.2f}'.rjust(7) + '\n'
        result += f'Total: {self.get_balance():.2f}'
        return result
           





def create_spend_chart(categories):
    withdrawls=[sum(i['amount']for i in cat.ledger if i['amount']<0) for cat in categories]
    total=sum(withdrawls)
    percentage = [math.floor(round(abs(w) / abs(total) * 100, 10) / 10) * 10 for w in withdrawls]   

    result = 'Percentage spent by category\n'

    for i in range(100,-1,-10):
        row=str(i).rjust(3)+"|"
        for p in percentage:
            if p>=i:
                row+=" o "
            else:
                row+="   "  
        row+=" \n" 
        result+=row 

    result += '    -' + '-' * (3 * len(categories)) + '\n'      

    max_length=max(len(cat.name)for cat in categories)
    

    for i in range(max_length):
      row = '     '
      for cat in categories:
        if i < len(cat.name):
            row += cat.name[i] + '  '
        else:
            row += '   '
      if i < max_length - 1:
           row += '\n'
      result += row
    return result

