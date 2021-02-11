#Create an add function that is agnostic to number of inputs

def My_Custom_Add(a):
    return sum(a)
n=[int(e) for e in input("Enter numbers to add(separated by spaces): ").split(" ")]
print("Sum of numbers is:",My_Custom_Add(n))