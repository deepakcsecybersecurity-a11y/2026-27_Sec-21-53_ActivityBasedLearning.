# Example rule: pass mark is 35 out of 100.
# A student may receive up to 3 grace marks to reach 35.

marks = [] #Creating a list on marks
subjects = ["English", "Maths", "Python"]

mark = int(input("Enter marks for " + subject + ": "))
for subject in subjects:
    if mark < 0 or mark > 100:
        print("Invalid marks. Enter a value from 0 to 100.")
        mark = int(input("Enter marks again for " + subject + ": "))
    marks.append(mark) #Adding mark in the list created before using append method

final_marks = []
failed = 0

for mark in marks:
    if mark < 35 and mark >= 32:
        mark = mark + 3
    final_marks.append(mark) # Adding mark in the final mark list
    if mark < 32:
        failed = failed + 1
print("Final marks:", final_marks)

if failed == 0:
    print("Result: PASS")
else:
    print("Result: FAIL")
    
print("Number of subjects failed:", failed)
