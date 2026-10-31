# Example rule: pass mark is 35 out of 100.
# A student may receive up to 3 grace marks to reach 35.

marks = []
subjects = ["English", "Maths", "Python"]

for subject in subjects:
    mark = int(input("Enter marks for " + subject + ": "))
    if mark < 0 or mark > 100:
        print("Invalid marks. Enter a value from 0 to 100.")
        mark = int(input("Enter marks again for " + subject + ": "))
    marks.append(mark)

final_marks = []
failed = 0

for mark in marks:
    if mark < 35 and mark >= 32:
        mark = mark + 3
    final_marks.append(mark)
    if mark < 35:
        failed = failed + 1

print("Final marks:", final_marks)

if failed == 0:
    print("Result: PASS")
else:
    print("Result: FAIL")
print("Number of subjects failed:", failed)
