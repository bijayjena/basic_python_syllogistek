#take a 2*2 square matrix as input and calculate the determinant

print("enter 2*2 square matrix elements:")
mat=[[int(input()) for i in range(2)] for j in range(2)]
# for item in mat:
#     print(item)
print("Determinant is",(mat[0][0]*mat[1][1])-(mat[0][1]*mat[1][0]))