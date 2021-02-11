#Implement the circle problem using object oriented approach

# a.Create a circle class
# b.Take center coordinates and radius as attributes
# c.Define all related functions within the class like
#     i.Area
#     ii.Perimeter
#     iii.Center distance from origin
#     iv.Circumference distance from origin
# d.Handle any exceptions and Not valid scenarios

class circle:
    def __init__(self,x,y,r):
        self.x=x
        self.y=y
        self.r=r
    # def get_r(self):
    #     return self.r
    # def set_r(self,r):
    #     self.r=r
    def area(self):
        return 3.142*self.r*self.r
    def perimeter(self):
        return 2*3.142*self.r
    def center_from_origin(self):
        return ((self.x**2) + (self.y**2))**0.5
    def circum_from_origin(self):
        return self.center_from_origin()-self.r

x=int(input("Enter the coordinate x of origin: "))
y=int(input("Enter the coordinate y of origin: "))
r=int(input("Enter the radius: "))
if(r<=0):
    print("Invalid Input!!")
else:
    c1=circle(x,y,r)
    print("Area =",c1.area())
    print("Perimeter =",c1.perimeter())
    print("Center Distance form Origin =",c1.center_from_origin())
    print("Circumference Distance form Origin =",c1.circum_from_origin())