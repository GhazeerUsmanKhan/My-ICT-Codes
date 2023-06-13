import random
import sys
import re

class ATM():
    def __init__(self, name, password, balance = 0):
        self.name = name
        self.password = password
        self.balance = balance+1000
         
    def account_detail(self):
        print("\n----------ACCOUNT DETAIL----------")
        print(f"Account Holder: {self.name.upper()}")
        print(f"Available balance: Rs.{self.balance}\n")
         
    def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print("Current account balance: Rs.", self.balance)
        print()
 
    def withdraw(self, amount):
        self.amount = amount
        if self.amount > self.balance:
            print("Insufficient fund!")
            print(f"Your balance is Rs.{self.balance} only.")
            print("Try with lesser amount than balance.")
            print()
        else:
            self.balance = self.balance - self.amount
            print(f"Rs.{amount} withdrawal successful!")
            print("Current account balance: Rs.", self.balance)
            print()
 
    def check_balance(self):
        print("Available balance: Rs.", self.balance)
        print()
 
    def transaction(self):
        print("""
            TRANSACTION 
        *********************
            Menu:
            1. Account Detail
            2. Check Balance
            3. Deposit
            4. Withdraw
            5. Exit
        *********************
        """)
        
        while True:
            try:
                option = int(input("Enter 1, 2, 3, 4 or 5:"))
            except:
                print("Error: Enter 1, 2, 3, 4, or 5 only!\n")
                continue
            else:
                if option == 1:
                    atm.account_detail()
                elif option == 2:
                    atm.check_balance()
                elif option == 3:
                    amount = int(input("How much you want to deposit(Rs.):"))
                    atm.deposit(amount)
                elif option == 4:
                    amount = int(input("How much you want to withdraw(Rs.):"))
                    atm.withdraw(amount)
                elif option == 5:
                    print(f"""
                printing receipt..............
          ******************************************
              Transaction is now complete.                         
               
              Account holder: {self.name.upper()}                  
              Available balance: Rs.{self.balance}                 
              Thanks for choosing us as your bank                  
          ******************************************
          """)
                    sys.exit()
                 
 
print("    Welcome to the Official Piggy Bank Fiduciary Application     ")
print("___________________________________________________________\n")
print("----------ACCOUNT CREATION----------")
name = input("Enter your name: ")

while True:
    password=input("Please enter the password for your account. Password needs to have at least 1 Uppercase, 1 Lowercase and 1 special character. Has to be a minimum of 8 letters. ")
    password_pattern = "^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$"
    x=re.match(password_pattern, password)
    if x:
        print("Your password is picture perfect. Please Continue.")
        break


print("Congratulations! Account created successfully......\n")
 
atm = ATM(name, password)
 
while True:
    trans = input("Do you want to do any transaction?(y/n):")
    if trans == "y":
        atm.transaction()
    elif trans == "n":
        print("""
    -------------------------------------
   | Thanks for choosing us as your bank |
   | Visit us again!                     |
    -------------------------------------
    Have fun with our Piggy
                             ████████████                                                            
          ██████  ██████░░░░░░░░░░░░██████    ██████                                            
        ██░░░░████░░░░░░░░░░░░░░░░░░░░░░░░████░░░░░░████                                        
      ██░░░░██▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒██░░░░░░▒▒██                                      
      ██░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██░░░░░░░░██                                    
    ██░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██░░░░░░░░████████████                          
    ██░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██░░░░░░██░░░░░░░░▒▒██████                    
    ██░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██░░░░░░██░░░░░░░░░░░░░░░░████                
      ████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██░░░░░░██░░░░░░░░░░░░░░░░░░░░██              
      ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██▓▓████▒▒░░░░░░░░░░░░░░░░░░░░▓▓██            
    ██░░░░██░░░░░░░░░░░░░░░░░░░░░░░░██░░░░░░░░░░░░░░░░░░██░░░░░░░░░░░░░░░░░░░░░░░░▒▒██      ████
  ██░░░░░░██░░░░██████░░░░░░░░░░░░░░██░░░░░░░░░░░░░░░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░██  ██░░██
  ██░░░░░░▓▓████░░░░░░████░░░░░░░░░░▓▓░░░░░░░░░░░░░░░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░██  ██░░██
  ██░░░░░░██░░░░░░░░░░░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██░░░░██
██░░░░░░██░░░░░░░░░░░░░░░░░░██░░░░░░░░░░░░░░  ░░░░░░░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██░░██  
██░░░░░░██░░░░██░░░░░░██░░░░██░░░░░░░░░░░░░░░░░░░░░░░░  ▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██    
██░░░░░░██░░░░██░░░░░░██░░░░██░░░░░░░░░░░░  ░░░░  ░░░░░░▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██    
██░░░░░░██░░░░░░░░░░░░░░░░░░██░░████░░░░░░░░░░░░░░░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██    
██░░░░░░▒▒████░░░░░░░░░░████░░░░██▒▒██░░░░░░░░░░░░░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██    
  ██░░░░░░▒▒▒▒██▓▓▓▓▓▓▓▓██████▓▓▓▓▓▓██░░░░░░░░░░░░░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██    
  ██░░░░░░░░░░░░░░░░██▓▓▓▓▓▓▓▓▓▓▓▓██░░  ░░░░░░░░░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██    
    ██░░░░░░░░      ░░████████████░░      ░░░░░░░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██    
      ██░░░░░░        ░░░░░░░░░░░░          ░░░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██    
        ██░░░░░░                            ░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██      
          ████░░░░                          ████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██      
              ████████                ██████░░▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██      
                      ████████████████░░▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██        
                        ██░░░░░░  ░░        ░░░░░░░░░░░░░░██            ██░░░░░░░░░░░░██        
                        ██░░░░░░██          ░░░░░░░░░░░░░░██            ██░░░░░░░░░░██          
                          ██░░░░░░████████████░░░░░░░░░░░░████████████████░░░░░░░░░░██          
                          ██░░░░░░░░██        ██░░░░░░░░██                ██░░░░░░██            
                            ██▓▓▓▓██            ██▓▓▓▓██                  ██▓▓▓▓██              
                              ████░░              ████                      ████                
                                                                                                
                                                                                                
                                                                                                
                                                                                                
                                                                                                
                                                                                                
    """)
        break
    else:
        print("Wrong command!  Enter 'y' for yes and 'n' for NO.\n")