#Check for Pallindrome in a string without using loop statement.
string = input("Enter string : ")
revers = string[::-1]
if(string.casefold() == revers.casefold()):
    print("It's pallindrome")
else:
    print("Not pallindrome")
