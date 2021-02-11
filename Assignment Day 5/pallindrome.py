string=input("Enter a string:")
i=0
f=1
while(i<len(string)/2):
    if(string[i]!=string[len(string)-i-1]):
        f=0
        break
    i+=1
if(f):
    print("It is pallindrome")
else:
    print("Not pallindrome")
