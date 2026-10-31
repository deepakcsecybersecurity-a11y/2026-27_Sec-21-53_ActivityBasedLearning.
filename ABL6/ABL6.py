students = ["Asha", "Rahul", "Neha"]
previous_marks = []
current_marks = []

for name in students:
    old =int(input("Enter previous exam marks for " + name + ": "))
    new = int(input("Enter current exam marks for " + name + ": "))
    previous_marks.append(old)
    current_marks.append(new)

for i in range(len(students)):
    change = current_marks[i] - previous_marks[i]
    print(students[i])
    print("Previous marks:", previous_marks[i])
    print("Current marks:", current_marks[i])

    if change > 0:
        print("Performance improved by", change, "marks")
    elif change < 0:
        print("Performance declined by", -change, "marks")
    else:
        print("Performance stayed the same")
