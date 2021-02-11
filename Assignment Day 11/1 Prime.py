#Write a function to check if input number is prime

def prime(n):
    if(n==1):
        return False
    count=0
    for i in range(2,n):
        if(n%i==0):
            count+=1
    if(count==0):
        return True
    else:
        return False
def main():
    n=int(input("Enter a positive number to check prime: "))
    if(prime(n)):
        print("{} is prime".format(n))
    else:
        print("{} is not prime".format(n))
    if(input("Do you want to check another? Y or N\n")=="y"):
        main()
main()