#Change the case of each character

x=input("Enter a string: ")
s=" "
for i in x:
    if (ord(i)>=97 and ord(i)<=122):
        s=s+chr(ord(i)-32)
    elif (ord(i)>=65 and ord(i)<=90):
        s=s+chr(ord(i)+32)
    else:
        s=s+i
print("Changed case:")
print(s)