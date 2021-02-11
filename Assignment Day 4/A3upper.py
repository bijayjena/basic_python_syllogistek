'''Write a program that accepts sequence of lines as input and prints the lines after
making all characters in the sentence capitalized. Suppose the following input is
supplied to the program'''

length=int(input("Enter the number of lines you want to input : "))
str_list=[]
for i in range(length):
    print("Enter the line ",i+1,":")
    str_list.append(input())
print("Capitalized sentences are : ")
for i in range(length):
    print(str_list[i].upper())
