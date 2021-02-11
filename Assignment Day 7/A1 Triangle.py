#Triangle problem

def is_valid(a,b,c):
    if(a<b+c and b<a+c and c<a+b):
        return True
    else:
        return False
def triangle_class(a,b,c):
    if(is_valid(a,b,c)):
        if(a==b==c):
            return "Equilateral"
        elif(a==(b**2+c**2)**0.5 or b==(a**2+c**2)**0.5 or c==(b**2+a**2)**0.5):
            return "Rightangled"
        elif(a==b or b==c or a==c):
            return "Isosceles"
        else:
            return "Scalene"
    else:
        return -1
def circumRadius(a,b,c):
    if triangle_class(a, b, c) == "Rightangled":
        if(a>b>c):
            return a/2
        elif(b>c>a):
            return b/2
        else:
            return c/2
    else:
        return -1
def main():
    a,b,c = input("Enter sides of triangle separated by spaces").split(" ")
    a,b,c = int(a),int(b),int(c)
    print(is_valid(a,b,c))
    print(triangle_class(a,b,c))
    print(circumRadius(a,b,c))
main()