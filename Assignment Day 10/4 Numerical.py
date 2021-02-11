#Consider a sorted sequence of number with following pattern
#2^i × 3^j × 5^k

n=int(input("Enter the range: "))
k=int(input("Enter the position: "))
ran=1
ls=[]
ls.append(ran)
while(ran<n):
    ran+=1
    if (ran%2==0 or ran%3==0 or ran%5==0) and ran%7!=0:
        ls.append(ran)
print(ls)
print(ls[k-1])