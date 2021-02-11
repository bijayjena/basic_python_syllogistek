x=int(input("Enter a number : "))
su = 0
if x>=0:
    while x!=0:
        d=x%10
        su = su + d
        x=x//10
    print("Sum of digits is : ",su)
else:
    print("Invalid input")
