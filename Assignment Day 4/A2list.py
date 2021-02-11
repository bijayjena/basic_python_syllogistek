'''Input a comma separated list from console. Write a program to print this list after
removing all duplicate values with original order reserved'''

list1=[]
list2=[]
list1=input("Enter the elements of the list separated by commas: ").split(',')
for i in list1:
    if i not in list2:
        list2.append(i)
print("Final list is",list2)




















































'''
lis=[int(ele) for ele in input("Enter the elements of the list separated by comma: ").split(",")]
for i in range(len(lis)):
    for j in range(i+1,len(lis)):
        if(lis[i]==lis[j]):
            lis[j].remove()
print("Final list is",lis)
'''
