x = int (input("Enter the x value : "))
y = int (input("Enter the y value : "))
r = int (input("Enter the radius : "))

area = 3.14 * (r**2)
peri = 2 * 3.14 * r
D = ((x**2) + (y**2))**0.5
d = D - r

print(area)
print(peri)
print(D)
print(d)
