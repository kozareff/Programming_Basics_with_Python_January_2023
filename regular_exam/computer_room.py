month = input()
hours = int(input())
people_in_group = int(input())
time_of_day = input()

price_per_one = 0

if month == 'march' or month == 'april' or month == 'may':
    if time_of_day == 'day':
        price_per_one = 10.5
    elif time_of_day == 'night':
        price_per_one = 8.4

elif month == 'june' or month == 'july'  or month == 'august':
    if time_of_day == 'day':
        price_per_one = 12.6
    elif time_of_day == 'night':
        price_per_one = 10.2

if people_in_group >= 4:
    price_per_one *= 0.9
    if hours >= 5:
        price_per_one *= 0.5

total_cost = hours * price_per_one * people_in_group

print(f'Price per person for one hour: {price_per_one:.2f}')
print(f"Total cost of the visit: {total_cost:.2f}")
