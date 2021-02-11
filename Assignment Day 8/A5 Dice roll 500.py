#Assume a fair dice roll using a similar random integer generation code above roll for
#500 times and print the number of times 1 to 6 has appeared

import random
list1=[random.randint(1,6) for i in range(500)]
c1=c2=c3=c4=c5=c6=0
d={}
for i in list1:
    if(i==1):
        c1+=1
        d.update({1:c1})
    elif(i==2):
        c2+=1
        d.update({2: c2})
    elif(i==3):
        c3+=1
        d.update({3: c3})
    elif(i==4):
        c4+=1
        d.update({4: c4})
    elif(i==5):
        c5+=1
        d.update({5: c5})
    else:
        c6+=1
        d.update({6: c6})
print(d)