# Example rates: first 100 units = Rs. 2/unit,
# next 100 units = Rs. 3/unit, above 200 = Rs. 5/unit.
# Fixed charge = Rs. 50
#taking input from the user
units = int(input("Enter electricity units used: "))

if units < 0: #if condition to check the units
    print("Units cannot be negative.")
else:
    if units <= 100:
        bill = units * 2
    elif units <= 200:
        bill = (100 * 2) + (units - 100) * 3
    else:
        bill = (100 * 2) + (100 * 3) + (units - 200) * 5

    bill = bill + 50
    print("Electricity bill = Rs.", bill)
