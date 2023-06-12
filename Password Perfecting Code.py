import re
import sys
import random
print("Welcome to the Official Piggy Bank Fiduciary Application. ")
a=input("Since I know you are a new initiate, please enter your signup Username. ")
b=input("Please enter the password for your account. Password needs to have at least 1 Uppercase, 1 Lowercase and 1 special character. Has to be a minimum of 8 letters. ")
while True:
    password_pattern = "^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$"
    x=re.match(password_pattern, b)
    if x:
        print("Your password is picture perfect. Please Continue.")
        break
    
   