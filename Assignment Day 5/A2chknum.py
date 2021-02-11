#Find if a number is present in a list 

list1=[int(ele) for ele in input("Input list separated by spaces: ").split(" ")]
n=int(input("Enter a number: "))
if(n in list1):
    print("{} is present in the list".format(n))