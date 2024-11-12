# Show net price with either 15% or 20% discount based on price

price = int(input("Enter price :"))

if price > 10000:
    discount = price * 20 // 100
else:
    discount = price * 15 // 100

net_price = price - discount

print(f'Net price = {net_price}')

