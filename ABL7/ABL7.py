#7. Advanced Numeric Pattern Generator (PDF Task 27)
n = int(input("Enter diamond size (1 to 9): "))

if n < 1 or n > 9:
    print("Enter a size from 1 to 9.")
else:
    # Upper half
    for i in range(1, n + 1):
        for space in range(n - i):
            print(" ", end="")
        for j in range(1, i + 1):
            print(j, end="")
        for j in range(i - 1, 0, -1):
            print(j, end="")
        print()

    # Lower half
    for i in range(n - 1, 0, -1):
        for space in range(n - i):
            print(" ", end="")
        for j in range(1, i + 1):
            print(j, end="")
        for j in range(i - 1, 0, -1):
            print(j, end="")
        print()
