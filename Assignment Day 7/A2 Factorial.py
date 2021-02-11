#Take integral numbers and calculate the factorial

def My_factorial(a):
    if(a==0):
        return 1
    elif(a<0):
        return -1
    f=1
    for i in range(1,a+1):
        f*=i
    return f
print(My_factorial(-1))
print(My_factorial(0))
print(My_factorial(1))
print(My_factorial(5))