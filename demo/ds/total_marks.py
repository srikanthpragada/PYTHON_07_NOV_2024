data = [ (1, 80), (2, 50), (1,75), (2, 70), (3, 79)]

students = {}

for t in data:
    rollno, marks = t
    if rollno in students:
        students[rollno] = students[rollno] + marks  # add marks to total
    else:
        students[rollno] = marks  # add new entry

print(students)


