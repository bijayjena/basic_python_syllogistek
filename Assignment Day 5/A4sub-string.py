#Find if the sub-string exists in the string without using in operator

str1=input("Input String: ")
str2=input("Input the sub-string you want to find: ")
if(str2==""):
    print("Empty string")
else:
    n=str1.find(str2)  #find gives 0 or more value if a sub-string is found
    if(n>=0):
        print("{} is found".format(str2))
    else:
        print("{} is not found".format(str2))