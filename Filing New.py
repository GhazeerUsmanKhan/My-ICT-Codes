f=open("first criminal.txt", "w")
f.write("This is my first trial for the Filing method, and after this I will be attempting input saving!")
f.close()
f=open("first criminal.txt", "r")
print(f.read())

filename=input("Enter Your File Name")
print(f'{filename}.txt') 
with open(f'{filename}.txt', 'w', encoding='utf-8') as f:
    f.write('first line' + '\n')
    f.write('second line' + '\n')
