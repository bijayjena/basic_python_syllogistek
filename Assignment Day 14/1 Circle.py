class circle:
    def __init__(self, x, y, r):
        self.__x = x
        self.__y = y
        self.r = r

    @property
    def r(self):
        return self.__r

    @r.setter
    def r(self, r):
        assert r > 0, "Radius can't be less than or equal to zero"
        self.__r = r

    def area(self):
        return 3.142 * self.__r * self.__r

    def perimeter(self):
        return 2 * 3.142 * self.__r

    def center_from_origin(self):
        return ((self.__x ** 2) + (self.__y ** 2)) ** 0.5

    def circum_from_origin(self):
        return self.center_from_origin() - self.__r

#Main
print("Enter coordinates and radius separated by spaces respectively:")
x, y, r = map(int, input().split())
c = circle(x, y, r)
print("Area:", c.area())
print("Perimeter:", c.perimeter())
print("Center from origin:", c.center_from_origin())
print("Circumference from origin", c.circum_from_origin())