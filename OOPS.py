class student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
s1 = student("Shub", 18)
s2 = student("Toji", 32)

print(s1.name, s1.age)
print(s2.name, s2.age)

class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
        
S1 = Car("BMW", 2020)
S2 = Car("TATA", 2023)

print(S1.brand, S2.year)
print(S2.brand, S1.year)

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def greet(self):
       print("Hi, My name is", self.name)
       
s1 = Student("Shub", 18)

s1.greet()

class Car:
       def __init__(self, brand,year):
           self.brand = brand
           self.year = year
           
       def info(self):
            print(self.brand, "was made in", self.year)
            
a1 = Car("BMW", 2020)
a1.info()

class Bankaccount:
        def __init__(self, owner, balance):
            self.owner = owner
            self.balance = balance
            
        def show_balance(self):
            print(self.owner, "has balance of", self.balance)
            
s1 = Bankaccount("Shub", 100000)
s2 = Bankaccount("Gojo", 500000)

s1.show_balance()
s2.show_balance()
        
class bankaccount:
       def __init__(self, owner, balance):
           self.owner = owner
           self.balance = balance
           
       def show_balance(self):
           print(self.owner, "has balance of", self.balance)
           
       def deposit(self, amount):
           self.balance += amount
       def withdraw(self, amount):
           self.balance -= amount
        
           
a1 = bankaccount("Shub", 30000)
a1.show_balance()
a1.deposit(2000)
a1.show_balance()
a1.withdraw(3000)
a1.show_balance()



a1.show_balance()
 
               
class Bankaccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        
    def show_balance(self):
        print(self.owner, "has balance", self.balance)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Deposit successful")
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
            if amount <= 0:
                print("Invalid withdrawal amount")
            elif amount > self.balance:
                print("Insufficient balance")
            else:
                self.balance -= amount
                print("Withdrawal successful")
            
            
a1 = Bankaccount("Shub", 10000)

a1.withdraw(3000)   # valid
a1.withdraw(20000)  # too much
a1.withdraw(-50)    # invalid
a1.deposit(5000)    # Valid
a1.deposit(-50)       

a1.show_balance()     

  

  
       
       



           
 
           

           
       
      
       
       
    
  