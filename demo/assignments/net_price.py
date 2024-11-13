# Calculate net price

price = int(input("Enter price :"))

if price > 10000:
    discount = price * 20 / 100
elif price > 5000:
    discount = price * 15 / 100
else:
    discount = price * 10 / 100

net_price = price - discount

print(f'Net price : {net_price}')



