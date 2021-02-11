#Accept two sequence of number, one for distance another for time and return a list of speeds

def speed(d,t):
    return d/t
dist=[int(e) for e in input().split(" ")]
time=[int(e) for e in input().split(" ")]
sp=[]
for i in range(len(dist)):
    sp.append(speed(dist[i],time[i]))
print(sp)