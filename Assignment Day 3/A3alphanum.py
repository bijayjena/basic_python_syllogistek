#to count letters and digits
s=input("Enter a string :")
l=0
d=0
for i in range (len(s)):
    if(s[i].isalpha()):
        l+=1
    elif(s[i].isdigit()):
        d+=1
print("LETTERS",l)
print("DIGITS",d)
