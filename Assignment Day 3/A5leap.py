#Write a program to find Leap year.

y=int(input("Enter a year : "))
if(y>0):
    if(y%400)==0:
        print(y,"is a leap year")
    elif (y%4)==0 and (y%100)!=0:
        print(y,"is a leap year")
    else:
        print(y,"is not a leap year")
else:
    print("Ivalid Input")
