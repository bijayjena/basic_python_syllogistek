# Run the code below to generate a matrix Approach:
#          take an input character as target
#          print the row index and column index
#          if the character is found Else print "Not found" 

table=[list("abcd"),list("efgh"),list("ijkl")]
target=input('Enter a target character to find from the matrix: ')
found=False
row=1
for i in table:
    column=1
    for j in i:
        if(j==target):
            print("Row:",row,"  Column:",column)
            found=True
            break
        column+=1
    row+=1
if(found):
    pass
else:
    print("Not found")