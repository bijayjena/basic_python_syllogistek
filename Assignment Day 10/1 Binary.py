#BInary Search using Recursion

def binary(list1,start,end,key):
    if (start>=end):
        return -1
    mid=(start+end)//2
    if(list1[mid]<key):
        return binary(list1,mid+1,end,key)
    elif(list1[mid]>key):
        return binary(list1,start,mid,key)
    else:
        return mid

list1=[int(ele) for ele in input("Input a sorted list: ").split(" ")]
key=int(input("Input the element you want to search in the list: "))
index=binary(list1,0,len(list1),key)
if(index<0):
    print("{} was not found".format(key))
else:
    print("{} was found at position {}".format(key,index+1))