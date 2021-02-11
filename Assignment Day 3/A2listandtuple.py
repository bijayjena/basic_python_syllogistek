#Print a list and tuple where the value is square of numbers between 1 and 20(both included)
list=[]
tupl=()
for i in range(1,21):
    list.append(i**2)
tupl=tuple(list)
print("List :")
print(list)
print("Tuple : ")
print(tupl)
