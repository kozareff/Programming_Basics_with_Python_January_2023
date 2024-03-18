type_flower = input()
flower_count = int(input())
budget = int(input())

ROZA_PRICE = 5
DALIA_PRICE = 3.8
LALE_PRICE = 2.8
NARCIS_PRICE = 3
GLADIOLA_PRICE = 2.5

if type_flower == 'Roses':
    price = flower_count * ROZA_PRICE
    if flower_count > 80:
        price *= 0.9

elif type_flower == 'Dahlias':
    price = flower_count * DALIA_PRICE
    if flower_count > 90:
        price *= 0.85

elif type_flower == 'Tulips':
    price = flower_count * LALE_PRICE
    if flower_count > 80:
        price *= 0.85

elif type_flower == 'Narcissus':
    price = flower_count * NARCIS_PRICE
    if flower_count < 120:
        price *= 1.15

elif type_flower == 'Gladiolus':
    price = flower_count * GLADIOLA_PRICE
    if flower_count < 80:
        price *= 1.2

if price <= budget:
    print(f'Hey, you have a great garden with {flower_count} {type_flower} and {budget - price:.2f} leva left.')
else:
    print(f'Not enough money, you need {price - budget:.2f} leva more.')