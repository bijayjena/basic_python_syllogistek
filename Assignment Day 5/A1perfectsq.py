#Check if a given input number is a perfect square

n=int(input("Enter a number to check if it is a perfect square: "))
if(n>0):
    s=n**0.5
    if(s//1==s):
        print(n,"is perfect square")
    else:
        print(n,"isn't perfect square")
else:
    print("Invalid Input")