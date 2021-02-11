#Check if the input is a valid integer

is_int=True
try:
    x=int(input("Input : "))
except ValueError:
    is_int=False
if(is_int):
    print("Integer Value")
else:
    print("Not an Integer")