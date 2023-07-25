f=open("first criminal.txt", "w")
f.write("This is my first trial for the Filing method, and after this I will be attempting input saving!")
f.close()
f=open("first criminal.txt", "r")
print(f.read())

dollarbills=input("Enter Your Name. ")
f=open("input saving trial.txt", "w")
f.write(dollarbills)
f.close()
f=open("input saving trial.txt", "r")
print(f.read())

