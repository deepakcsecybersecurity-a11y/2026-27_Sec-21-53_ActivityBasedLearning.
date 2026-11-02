# Example rule: 10% discount when subtotal is Rs. 1000 or more.
# Tax is 5% after discount.
# Taking input from the user
n = int(input("How many products? "))
subtotal = 0


name = input("Enter product name: ")
price = float(input("Enter price: Rs. "))
quantity = int(input("Enter quantity: "))
amount = price * quantity
subtotal = subtotal + amount
print(name, "amount = Rs.", amount)
for i in range(n):
    if subtotal >= 1000:
        discount = subtotal * 0.10
    else:
        discount = 0

after_discount = subtotal - discount
tax = after_discount * 0.05
total = after_discount + tax

print("Subtotal = Rs.", subtotal)
print("Discount = Rs.", discount)
print("Tax = Rs.", tax)
print("Final bill = Rs.", total)
