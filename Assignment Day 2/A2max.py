list = []
len=int(input("Enter the length of the list : "))
print("Enter the elements : ")
for i in range (len) :
    list.append(int(input()))
maxi=list[0]
for i in range (1,len) :
    if maxi<list[i]:
        maxi=list[i]
print("Maximum element is ",maxi)
