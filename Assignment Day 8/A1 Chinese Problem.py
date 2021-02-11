#Write a program to solve a classic ancient Chinese puzzle: We count 35 heads and94 legs
#among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have?

def solve(h,l):
    c=r=0
    a=False
    for i in range(h+1):
        j=h-i
        if (2*i)+(4*j)==l:
            c=i
            r=j
            a=True
            break
    if a==True:
        print("Chickens : ",c)
        print("Rabbit : ",r)
    else:
        print("ERROR")
if __name__ == '__main__':
    h=int(input("Enter the no of heads: "))
    l=int(input("Enter the no of legs: "))