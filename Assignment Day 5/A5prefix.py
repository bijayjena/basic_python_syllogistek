#Given a list of strings find the longest common prefix for them 

list1=input("Input string separated by spaces: ").split(" ")
n=len(list1)
prefix=list1[0]
for i in range(1,n):
    str1=list1[i]
    res=""
    l1=len(prefix)
    l2=len(str1)
    j=0
    k=0
    while j<l1 and k<l2:
        if(prefix[j]!=str1[k]):
            break
        res+=prefix[j]
        j+=1
        k+=1
    prefix=res
if(len(prefix)):
    print("The common prefix is",prefix)
else:
    print("There is no common prefix")
