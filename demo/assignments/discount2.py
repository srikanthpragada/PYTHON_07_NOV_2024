# Calculate discount

# input
price = int(input("Enter price :"))

# process
discount = price * 15 // 100
net_price = price - discount

#output
print(f"Price     {price:8}")
print(f"Discount  {discount:8}")
print(f"Net Price {net_price:8}")

