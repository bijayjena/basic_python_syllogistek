#Write a program to find palindromic numbers between 2 numbers

x=int(input("Enter the no.s between which you want pallindromic no.s : "))
y=int(input())
if(x>y):
    t=x
    x=y
    y=t
p_list=[]
for i in range(x,y):
    org=i
    rev=0
    while(i!=0):
        t=i%10
        rev=rev*10+t
        i=i//10
    if(org==rev):
        p_list.append(org)
print("Pallindromic numbers are :",p_list)
