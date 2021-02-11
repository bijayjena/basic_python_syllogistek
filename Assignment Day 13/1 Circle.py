#Given attributes (x,y,r) for two circles identify if the circles "intersect", "touch" or "Not intersect"
#exmple of touch: 1 1 3 and 5 4 2

class circle:
    def __init__(self,x,y,r):
        self.x=x
        self.y=y
        self.r=r

def identify(c1,c2):
    d=((c2.x-c1.x)**2 + (c2.y-c1.y)**2)**0.5
    r_sum=c1.r+c2.r
    if(d==r_sum):
        return "touch"
    elif(d<r_sum):
        return "intersect"
    else:
        return "not intersect"
#Main
x,y,r=input("Input x,y and r values of circle 1: ").split()
x,y,r=int(x),int(y),int(r)
c1=circle(x,y,r)
x,y,r=input("Input x,y and r values of circle 2: ").split()
x,y,r=int(x),int(y),int(r)
c2=circle(x,y,r)
print("The circles does "+identify(c1,c2))