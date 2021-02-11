class triangle:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        assert (self.__x < self.__y + self.__z and self.__y < self.__x + self.__z and self.__z < self.__x + self.__y), "Triangle Invalid"

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        assert x > 0, "Side can't be less than or equal to zero"
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        assert y > 0, "Side can't be less than or equal to zero"
        self.__y = y

    @property
    def z(self):
        return self.__z

    @z.setter
    def z(self, z):
        assert z > 0, "Side can't be less than or equal to zero"
        self.__z = z

    def area(self):
        s = self.perimeter() / 2
        return (s * (s - self.x) * (s - self.y) * (s - self.z)) ** 0.5

    def perimeter(self):
        return self.x + self.y + self.z


# Main
print("Enter sides respectively:")
x, y, r = map(int, input().split())
t = triangle(x, y, r)
print("Area:", t.area())
print("Perimeter:", t.perimeter())