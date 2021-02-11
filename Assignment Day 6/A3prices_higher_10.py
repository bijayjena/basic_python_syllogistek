#Given a list of products, print out the name of all the products with a price higher than 10

products={'orange':20,'apple':8,'banana':10,'kiwi':30}
print("The products above price 10 are:")
for i,j in products.items():
    if j>10:
        print(i,":",j)

















"""
products=input("Enter the products:").split(",")
prices=input("Enter the prices:").split(",")
for i,j in zip(products,prices):
    if (int(j)>10):
        print(i,j)

"""