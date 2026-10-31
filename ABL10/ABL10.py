#10. Tuple-Based Product Catalogue Audit (PDF Task 49)
# Each tuple contains: product name, price, stock quantity
products = [
    ("Pen", 10, 50),
    ("Notebook", 40, 8),
    ("Bag", 700, 3),
    ("Pencil", 5, 0)
]

minimum_stock = int(input("Enter minimum stock level: "))
total_value = 0

for product in products:
    name, price, quantity = product
    value = price * quantity
    total_value = total_value + value

    print("Product:", name)
    print("Price: Rs.", price)
    print("Quantity:", quantity)
    print("Stock value: Rs.", value)

    if quantity == 0:
        print("Status: Out of stock")
    elif quantity < minimum_stock:
        print("Status: Replenishment needed")
    else:
        print("Status: Stock sufficient")
    print()

print("Total inventory value = Rs.", total_value)
