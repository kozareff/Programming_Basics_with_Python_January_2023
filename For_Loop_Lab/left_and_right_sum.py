import math

n = int(input())
left_sum = 0
right_sum = 0

for i in range(0, n):
    numbersForLeftSide = int(input())
    left_sum += numbersForLeftSide

for i in range(0, n):
    numbersForRightSide = int(input())
    right_sum += numbersForRightSide

if left_sum == right_sum:
    print('Yes, sum = %d' % left_sum)
else:
    print('No, diff = %d' % math.fabs(right_sum - left_sum))



#мисля че двете са едно и също

input_count = int(input())

left_num = 0
right_num = 0

for i in range(0, input_count):
    num = int(input())
    left_num += num
for i in range(0, input_count):
    num = int(input())
    right_num += num

if left_num == right_num:
    print(f'Yes, sum = {left_num}')
elif left_num > right_num or left_num < right_num:
    print(f'No, diff = {abs(left_num - right_num)}')