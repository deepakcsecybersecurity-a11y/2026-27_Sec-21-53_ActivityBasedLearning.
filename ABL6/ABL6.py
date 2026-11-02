students = ["Asha", "Rahul", "Neha"]
previous_marks = [] # Creating a list on the previous marks of the students
current_marks = [] # Creating a list on the Current marks of the students

for name in students:
    old =int(input("Enter previous exam marks for " + name + ": "))
    new = int(input("Enter current exam marks for " + name + ": "))
# Adding the marks of the students to the respective lists using the append method
    previous_marks.append(old)
    current_marks.append(new)

for i in range(len(students)):
    change = current_marks[i] - previous_marks[i]
    print(students[i]) # Here " i " represents the name of the student
    print("Previous marks:", previous_marks[i]) # here "i" gives the previous marks of the student
    print("Current marks:", current_marks[i]) # here "i" gives the current marks of the student

    if change > 0:
        print("Performance improved by", change, "marks")
    elif change < 0:
        print("Performance declined by", -change, "marks")
    else:
        print("Performance stayed the same")
