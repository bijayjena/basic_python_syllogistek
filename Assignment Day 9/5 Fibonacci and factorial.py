#Run a program to demonstrate Fibonacci and Factorial through recursion 

def factorial(x):
    if(x<=1):
        return 1
    else:
        return x*factorial(x-1)
def fibonacci(x):
    if(x<=1):
        return x
    else:
        return fibonacci(x-1)+fibonacci(x-2)
    #fibonacci series: 0 1 1 2 3 5 8 13 ....
x=int(input('Enter a positive number: ')) 
print('Factorial of',x,' is: ',factorial(x))
print('The',x,'th number in the fibonacci sequence is: ',fibonacci(x-1))