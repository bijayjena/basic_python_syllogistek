x=int(input("Enter the 1st number : "))
y=int(input("Enter the 2nd number : "))
while x!=0:
    t=y;
    y=x;
    x=t%x;
print("GCD is : ",y)
