def percent(marks):
    a = ((marks[0] + marks[1] + marks[2] + marks[3])/400)*100
    return a
marks1 = [67, 89, 65, 78]
percentage1 = percent(marks1)

marks2 = [56, 75, 73, 53]
percentage2 = percent(marks2)
print(percentage1, percentage2)


