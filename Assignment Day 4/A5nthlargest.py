#Given a list A and a number n, find the n’th largest number

A=[]
l=int(input("Enter the length of the list : "))
print("Enter the elements : ")
for i in range (l) :
    A.append(int(input()))
A.sort()
n=int(input("Enter the rank of largest number to find:"))
print("The",n,"th largest number is",A[-n])
