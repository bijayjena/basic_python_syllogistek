# Create a custom exception

class CustomException(BaseException):
    pass


# Main
a = int(input("Enter a positive number "))
if a < 0:
    raise CustomException
print("No exceptions")