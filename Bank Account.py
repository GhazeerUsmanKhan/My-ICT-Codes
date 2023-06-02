print("Welcome to the Official Piggy Bank Fiduciary Application. ")
a=input("Since I know you are a new initiate, please enter your signup Username. ")
b=input("Please enter the password for your account. You can trust us that no one is breaching your privacy. ")
print("Since you are a new initiate, we have decided to provide you with Rs.1000 extra. ")
reconfirmpass=input("Please reconfirm your password. ")
if reconfirmpass==b:
        print("This Password is also the same, you may continue with your banking options. ")
if reconfirmpass==b:
    try:
        bankingopt1=int(input("Press 1 to see your banking info, and 2 to skip ahead. "))

if bankingopt1==1:
    print("As of now, you have Rs1000 in your account, with no deposits made. ")
if bankingopt1==2:
    print("Skipping Ahead. ")
elif bankingopt1!=1 and bankingopt1!=2:
    print("This input is invalid. Please restart the Program. ")
if reconfirmpass==b:
    bankingopt2=int(input("Press 1 if you wish to deposit something in your account, Press 2 to skip ahead. "))
if bankingopt2==1:
    try:
        deposit=int(input("Please Enter the Deposit Amount. "))
    except ValueError:
        print("Your input is not an integer, please try again. ")
if bankingopt2==2:
    print("Skipping Ahead. ")
elif bankingopt2!=1 and bankingopt2!=2:
    print("This input is valid, please try again. ")
cashamount=deposit+1000
if reconfirmpass==b:
    bankingopt3=int(input("Press 1 for Cash Withdrawal, Press 2 to end Program. "))
if bankingopt3==1:
    try:
        withdraw=int(input("How much cash do you wish to withdraw. "))
    except ValueError:
        print("Your input is not an integer, please try again. ")
if withdraw>cashamount:
    print(" By withdrawing this amount, you are willingly going into debt with the bank. Press Enter to agree. ")
if bankingopt3==2:
    print("Exiting program. Please visit the Piggy Bank Fiduciary again! ")
elif bankingopt3!=1 and bankingopt3!=2:
    print("Your input is invalid. Please try again. ")
endamount=cashamount-withdraw
print("Thank you for Banking with the Piggy Bank Fiduicary application. Your cash amount with deposit was", cashamount,", and your end amount with withdrawal was ", endamount,". Please email us for any issues, and press Enter to exit the Program. ")