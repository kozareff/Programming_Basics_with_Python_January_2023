budget = float(input())
statists = int(input())
clothes_per_person = float(input())

decor = budget * 0.1

if statists > 150:
    clothes_per_person *= 0.9

money_needed = decor + statists * clothes_per_person

if money_needed <= budget:
    print('Action!')
    print(f'Wingard starts filming with {budget - money_needed:.2f} leva left.')
else:
    print('Not enough money!')
    print(f'Wingard needs {money_needed - budget:.2f} leva more.')

