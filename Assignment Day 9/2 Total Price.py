#Take two list of numbers of products quantities and prices and calculate total price

product_quantities=input('Enter the quantities of the products: ').split(" ")
price=input('Enter the prices of the products entered (respectiverly): ').split(" ")
total_price=[]
count=0
for o in product_quantities:
    total_price.append(int(product_quantities[count])*float(price[count]))
    count+=1
print('Total=',sum(total_price))