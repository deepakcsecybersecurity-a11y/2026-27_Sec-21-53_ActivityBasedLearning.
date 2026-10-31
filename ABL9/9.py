#9. Student Marks Matrix Analysis (PDF Task 42)
# Each row contains marks for one student.
marks = [
    [78, 85, 90],
    [65, 70, 68],
    [92, 88, 95]
]
names = ["Asha", "Rahul", "Neha"]
subjects = ["English", "Maths", "Python"]

for i in range(len(marks)):
    total = 0
    for j in range(len(marks[i])):
        total = total + marks[i][j]
    average = total / len(marks[i])
    print(names[i], "total =", total, "average =", average)

for j in range(len(subjects)):
    total = 0
    for i in range(len(marks)):
        total = total + marks[i][j]
    average = total / len(marks)
    print(subjects[j], "average =", average)

top_index = 0
for i in range(1, len(marks)):
    if sum(marks[i]) > sum(marks[top_index]):
        top_index = i

print("Top performer:", names[top_index])
