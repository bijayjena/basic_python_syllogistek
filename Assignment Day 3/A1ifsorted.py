#Find if a list is sorted in increasing order.
list=[]
length=int(input("Enter the length of list : "))
print("Input list : ")
for i in range (length):
    list.append(int(input()))
f=0
i=1
while i<length: 
    if(list[i]<list[i-1]): 
        f=1
    i+=1
if(not f): 
    print("Yes, List is sorted in increasing order.") 
else : 
    print("No, List is not sorted in increasing order.")
