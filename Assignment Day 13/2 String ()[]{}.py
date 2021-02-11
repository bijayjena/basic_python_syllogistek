#Given a string containing just the characters '(', ')', '{', '}', '['and ']', determine if the input string is valid

def validate(str1):
    flag=True
    for i in range(0,len(str1),2):
        if(str1[i]=='('):
            if(str1[i+1]!=')'):
                flag=False
        elif (str1[i] == '{'):
            if (str1[i + 1] != '}'):
                flag = False
        elif (str1[i] == '['):
            if (str1[i + 1] != ']'):
                flag = False
        else:
            flag=False
    if(flag):
        return "Valid"
    else:
        return "Not valid"
#Main
str1=input("Input the string containing () {} [] : ")
print(validate(str1))