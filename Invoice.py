product1_name, product1_price = input("Enter The item Name of 1st product"),input("Enter The item price of 1st product")
product2_name, product2_price = input("Enter The item Name of 2st product"),input("Enter The item price of 2st product")
product3_name, product3_price = input("Enter The item Name of 3st product"),input("Enter The item price of 3st product")
product4_name, product4_price = input("Enter The item Name of 4st product"),input("Enter The item price of 4st product")

ShopName = input("Enter your shop Name")
ShopAddress = input("Enter the shop Address")
ShopCity = input("Enter the Shop City")

message = "Thanks for shopping with us"
print("="*40)

print('\t\t{}'.format(ShopName.title()))
print('\t\t{}'.format(ShopAddress.title()))
print('\t\t{}'.format(ShopCity.title()))
print("#"*40)

print('\t{}\t\t₹{}'.format(product1_name.title(), product1_price))
print('\t{}\t\t₹{}'.format(product2_name.title(),product2_price))
print('\t{}\t\t₹{}'.format(product3_name.title(),product3_price))
print('\t{}\t\t₹{}'.format(product4_name.title(),product4_price))

print('*'*40)
print('\t\t\tTotal')

total = product1_price + product2_price + product3_price + product4_price
print('\t\t\t₹{}'.format(round(total,3)))
print('#'*40)
print('\n\t{}\n'.format(message))
print("^"*40)
