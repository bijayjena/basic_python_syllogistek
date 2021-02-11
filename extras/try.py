#Write a function to check if input number is prime
from pip._vendor.distlib.compat import raw_input


def prime(n):
    if n==1:
        return False
    count=0
    for i in range(2,n):
        if n%i==0:
            count+=1
    if count==0:
        return True
    else:
        return False
def main():
    n,r=map(int,raw_input("Enter a positive range of numbers to check prime: "))
    for i in range(n,r+1):
        if prime(n):
            print("{} is prime".format(n))
        else:
            print("{} is not prime".format(n))
main()