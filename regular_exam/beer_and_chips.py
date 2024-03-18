import math

name = input()
budget = float(input())
beers = int(input())
chips_count = int(input())

BEER_PRICE = 1.2
money_beer = BEER_PRICE * beers
chips_price = money_beer * 0.45
all_chips = math.ceil(chips_price * chips_count)
money_needed = all_chips + money_beer

dif = abs(money_needed - budget)
if budget >= money_needed:
    print(f'{name} bought a snack and has {dif:.2f} leva left.')
else:
    print(f'{name} needs {dif:.2f} more leva!')