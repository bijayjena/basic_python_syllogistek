#Remove if there are any duplicates

x=input("Enter a string: ")
s=" "
for i in x.split():
    if i not in s:
        s=s+i+" "
print("Duplicates removed:")
print(s)