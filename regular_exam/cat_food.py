number_of_cats = int(input())

PRICE_PER_KG_FOOD = 12.45

small_cats = 0
large_cats = 0
fat_cats = 0
eaten_food = 0
for cats in range(number_of_cats):
    food = float(input())
    if 100 <= food < 200:
        small_cats += 1
        eaten_food += food
    elif 200 <= food < 300:
        large_cats += 1
        eaten_food += food
    elif 300 <= food < 400:
        fat_cats += 1
        eaten_food += food

money_for_food = (eaten_food / 1000) * PRICE_PER_KG_FOOD


print(f'Group 1: {small_cats} cats.')
print(f'Group 2: {large_cats} cats.')
print(f'Group 3: {fat_cats} cats.')
print(f'Price for food per day: {money_for_food:.2f} lv.')
