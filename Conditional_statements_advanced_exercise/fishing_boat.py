budget = int(input())
season = input()
fishers_count = int(input())

if season == 'Spring':
    cost = 3000
elif season == 'Winter':
    cost = 2600
else:
    cost = 4200

if fishers_count <= 6:
    cost *= 0.9
elif 7 < fishers_count <= 11:
    cost *= 0.85
else:
    cost *= 0.75

if fishers_count % 2 == 0 and season != 'Autumn':
    cost *= 0.95

if cost <= budget:
    print(f'Yes! You have {budget - cost:.2f} leva left.')
else:
    print(f'Not enough money! You need {cost - budget:.2f} leva.')