#write a program that takes two matrices as input and does matrix multiplication

r1,c1=input("Enter number of rows and columns of matrix 1:").split()
r1,c1=int(r1),int(c1)
print("Enter elements:")
x=[[int(input()) for i in range(c1)] for j in range(r1)]
# for item in x:
#     print(item)
r2,c2=input("Enter number of rows and columns of matrix 2:").split()
r2,c2=int(r2),int(c2)
print("Enter elements:")
y=[[int(input()) for i in range(c2)] for j in range(r2)]
# for item in y:
#     print(item)
result=[[0 for i in range(c2)] for j in range(r1)]
for i in range(len(x)):
    for j in range(len(y[0])):
        for k in range(len(y)):
            result[i][j]+=x[i][k]*y[k][j]
print("Result:")
for item in result:
    print(item)