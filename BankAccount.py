# Benjamin Guth 
# Step by step 
# DS_WE1_Classes_AlgAnalysis
# 	BankAccount, BankAccount_transaction_fee and BankAccount_str 

class BankAccount: 
    #name = "Unamed account"
    #balance = 0.0 
    #transaction_fee = 0.0
    #new_fee = 0.0

    def __init__ (self, name):
        self.name = name
        self.balance = 0.0
        self.transaction_fee = 0.0


    def deposit (self, amount):
        if amount > 0:
            self.balance += amount

    def withdraw (self, amount):
        if self.transaction_fee >= 0:
            if amount > 0 and (amount + self.transaction_fee) <= self.balance:
                self.balance -= (amount + self.transaction_fee)
    
    @property
    def transaction_fee(self):
        return self._transaction_fee

    @transaction_fee.setter
    def transaction_fee(self, value):
        if value >= 0:
            self._transaction_fee = value
    
    
    
    
    
    #def setattr (self, choice, value ):
    #    tf = "transaction_fee"
    #    if choice == tf: 
    #        if value >= 0:
    #            self.transaction_fee = value
    #    else: 
    #        super().__setattr__ (choice, value)
            
    

    def __str__(self):
        
       new_string = self.name + ", $" +  "{:.2f}".format(  self.balance )
        
       return new_string

    """Add a __str__ method to the class that returns a string containing the account's name and balance separated by a comma and space. 
    Round the balance to two digits after the decimal point. 
    For example, if an account object named yana has the name "Mariana" and a balance of 3.5 (representing $3.50), 
    the call str(yana) should return the string "Mariana, $3.50". 
    Submit only your __str__ method, not the complete class. """

    

    #def set_transaction_fee ( self, transaction_fee):
     #   if transaction_fee >= 0:
      #      self.transaction_fee = transaction_fee

    #def transaction_fee (self, new_fee):
    #    if new_fee >= 0:
    #        self.transaction_fee = new_fee

#    def __setattr__  (transaction_fee, float, new_fee):
#        new_fee = float(new_fee)
#        if new_fee >= 0:
#            self._transaction_fee = new_fee

# test code

tuna = BankAccount("ben")

print(tuna.name, tuna.balance)

tuna.deposit(500)

print(tuna.name, tuna.balance) 

tuna.withdraw(400)
print(tuna.name, tuna.balance) 


print( )

#tuna.__set__(tuna, tuna.transaction_fee, -5)

#print ( tuna.__getattribute__("transaction_fee") )
 
#tuna.setattr  ("transaction_fee", -5) 

#print ( tuna.__getattribute__("transaction_fee") )

#print (tuna.name, tuna.balance, tuna.transaction_fee) 
print (tuna.__str__())
