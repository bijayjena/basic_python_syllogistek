#Give a list of weight and value pairs for items and a bag with capacity
#Sample: i/p:[(60,10),(100,20),(120,30)] o/p:240.0

items = list(tuple(map(int,input().split())) for r in range(int(input("Enter the number of pairs you want to input: "))))
capacity=int(input("Input Capacity:"))
values=[(a/b,b)for a,b in items]
values.sort(reverse=True,key=lambda value:value[0])
#print(values)
tot=0
for item in values:
    if item[1]<=capacity:
        tot=tot+item[0]*item[1]
        capacity=capacity-item[1]
    else:
        tot=tot+item[0]*capacity
        break
print(tot)