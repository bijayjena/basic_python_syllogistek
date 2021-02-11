#With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that
# is an integral number between 1 and n (both included) and then the program should print the dictionary.

def sq_dict(n):
    if(n>0):
        dict1={i:i*i for i in range(1,n+1)}
        return dict1
    else:
        print("Invalid Input")
        return -1
def main():
    n=int(input("Input the value of n till which the dictionary go: "))
    print(sq_dict(n))
main()