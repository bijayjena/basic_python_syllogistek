'''Write a program that can accept two strings as input and print the string with
maximum length in console. If two strings have the same length, then the
program should print both the strings line by line'''

s1=input("Enter String 1: ")
s2=input("Enter String 2: ")
if(len(s1)==len(s2)):
    print(s1)
    print(s2)
elif(len(s1)>len(s2)):
    print(s1)
else:
    print(s2)
