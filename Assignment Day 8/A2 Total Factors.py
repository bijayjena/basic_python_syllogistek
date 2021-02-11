#Find the total factors for a given integer N.

def total_factor(N):
    if(N>=0):
        list1=[]
        for i in range(1,N+1):
            if(N%i==0):
                list1.append(i)
        return len(list1)
    else:
        print("\nInvalid input!")
        return -1
def main():
    N=int(input("Enter the number to find the total number of factors: "))
    print("Total number of factors is:",total_factor(N))
main()