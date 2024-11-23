data = [ (1, 80), (2, 50), (1,75), (2, 70), (3, 79)]

students = {}

for t in data:
    rollno, marks = t
    total = students.get(rollno,0)
    students[rollno] = total + marks

print(students)


