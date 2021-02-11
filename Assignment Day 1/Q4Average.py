list = []
len=int(input("Enter the length of the list : "))
print("Enter the elements : ")
for i in range (len) :
    list.append(int(input()))
print("Average : ",sum(list)/len)
