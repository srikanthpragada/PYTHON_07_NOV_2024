
f = open("marks.txt", "rt")

plus_80 = 0
plus_60 = 0
below_60 = 0

for line in f:
    marks = int(line)
    if marks > 80:
        plus_80 += 1
    elif marks > 60:
        plus_60 += 1
    else:
        below_60 += 1

f.close()

print(f'Above 80  : {plus_80}')
print(f'Above 60  : {plus_60}')
print(f'<= 60     : {below_60}')

