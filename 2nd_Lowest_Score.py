def enter_class():
    class_grades = []
    for _ in range(int(input("# of Students? "))):
        name = input("Name? ")
        score = float(input("Grade? "))
        class_grades.append([name, score])
    print(class_grades)

class_grades = [['Bill', 42.0],['Jane', 32.0],['Oscar', 56.5]]
grades = sorted([a[1] for a in class_grades])
i = 1
while grades[i] == grades[0]:
    i += 1
sec_low = [a for a, b in sorted(class_grades) if b == grades[i]]
for name in sec_low:
    print(name)

marksheet = [['Bill', 42.0],['Jane', 32.0],['Oscar', 56.5]]
second_highest = sorted(list(set([marks for namer, marks in marksheet])))[1]
print('\n'.join([a for a, b in sorted(marksheet) if b == second_highest]))
