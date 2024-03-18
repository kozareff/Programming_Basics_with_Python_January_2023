from math import ceil

name_of_series = input()
series_lenght = int(input())
break_time = int(input())

lunch_break = break_time / 8
free_time = break_time / 4

time_needed = lunch_break + free_time + series_lenght
time_left = break_time - time_needed

if time_left >= 0:
    print(f'You have enough time to watch {name_of_series} and left with {ceil(time_left)} minutes free time.')
else:
    print(f"You don't have enough time to watch {name_of_series}, you need {ceil(abs(time_left))} more minutes.")

