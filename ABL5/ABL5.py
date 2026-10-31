balance = float(input("Enter opening balance: Rs. "))
transactions = []
n = int(input("How many transactions? "))

for i in range(n):
    print("1. Deposit")
    print("2. Withdraw")
    choice = int(input("Choose transaction: "))
    amount = float(input("Enter amount: Rs. "))

    if amount <= 0:
        print("Invalid amount.")
        transactions.append("Rejected transaction")
    elif choice == 1:
        balance = balance + amount
        transactions.append("Deposit: " + str(amount))
        print("Deposit successful.")
    elif choice == 2:
        if amount <= balance:
            balance = balance - amount
            transactions.append("Withdrawal: " + str(amount))
            print("Withdrawal successful.")
        else:
            print("Insufficient balance.")
            transactions.append("Rejected withdrawal")
    else:
        print("Invalid choice.")
        transactions.append("Invalid choice")

print("Transaction summary:")
for item in transactions:
    print(item)
print("Final balance = Rs.", balance)
