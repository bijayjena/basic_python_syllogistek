#Take two list of numbers and generate a list of tuples that are
#combo of the numbers such that two numbers in the pair are not equal

x = input('Enter the first list of numbers: ').split(" ")
y = input('Enter the second list of numebrs: ').split(" ")
t = [(int(i),int(j)) for i in x for j in y if(i!=j)]
print(t)