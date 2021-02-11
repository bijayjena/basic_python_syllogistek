#Remove if there are any special characters

x=input("Enter a string: ")
s=" "
for i in x:
    if(ord(i)>=97 and ord(i)<=122 or ord(i)==32 or ord(i)>=65 and ord(i)<=90):
        s=s+i
print("Special characters removed:")
print(s)