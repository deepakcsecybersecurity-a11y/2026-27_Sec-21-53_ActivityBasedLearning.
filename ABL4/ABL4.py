attended = int(input("Classes attended so far: "))
conducted = int(input("Total classes conducted so far: "))
target = float(input("Required attendance percentage: "))

if conducted <= 0 or attended < 0 or attended > conducted:
    print("Invalid attendance details.")
elif target <= 0 or target > 100:
    print("Target must be above 0 and at most 100.")
else:
    extra = 0
    while (attended + extra) * 100 / (conducted + extra) < target:
        extra = extra + 1

    print("Consecutive classes to attend:", extra)
