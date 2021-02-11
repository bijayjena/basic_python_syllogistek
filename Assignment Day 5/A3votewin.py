#Give a list of tickets for candidates, find out who is the winner 

lis=input("Input list separated by space: ").split(" ")
set1=set(lis)
set2=set(lis)
len_set=len(set1)
vote={}
for i in range(len(set1)):
    c=0
    t=set1.pop()
    for j in range(len(lis)):
        if(t==lis[j]):
            c+=1
    vote.update({t:c})
print("Here there are total {} candidates contesting".format(len_set),end=" ")
print(set2)
print("And winner is '{}' as he got the highest votes".format(max(vote,key=vote.get)))