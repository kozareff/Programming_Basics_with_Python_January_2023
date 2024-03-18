students = int(input())

top_student = 0
between_four_and_five = 0
between_three_and_four = 0
fail = 0
grade_sum = 0

for _ in range(1, students + 1):
    grade_per_student = float(input())
    grade_sum += grade_per_student

    if grade_per_student <= 2.99:
        fail += 1

    elif grade_per_student <= 3.99:
        between_three_and_four += 1

    elif grade_per_student <= 4.99:
        between_four_and_five += 1

    elif grade_per_student >= 5:
        top_student += 1


percent_top = (top_student / students) * 100
percent_four_five = (between_four_and_five / students) * 100
percent_three_four = (between_three_and_four / students) * 100
percent_fail = (fail / students) * 100

average_grade = grade_sum / students

print(f'Top students: {percent_top:.2f}%')
print(f'Between 4.00 and 4.99: {percent_four_five:.2f}%')
print(f'Between: 3.00 and 3.99: {percent_three_four:.2f}%')
print(f'Fail: {percent_fail:.2f}%')
print(f'Average: {average_grade:.2f}')