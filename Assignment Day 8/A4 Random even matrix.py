# generate a matrix as an input and print all the even numbers in it

import random
mat = [[random.randint(1,10) for i in range(4)] for row in range(4)]
print(mat)
for i in range(4):
    for j in range(4):
        if(mat[i][j]%2==0):
            print(mat[i][j],end=" ")