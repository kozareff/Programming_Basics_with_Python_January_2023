vacation_price = float(input())
puzzle_volume = int(input())
dolls_volume = int(input())
bears_volume = int(input())
minions_volume = int(input())
trucks_volume = int(input())

bonus = 0

PUZZLE_PRICE = 2.60
DOLL_PRICE = 3.00
BEAR_PRICE = 4.1
MINION_PRICE = 8.2
TRUCK_PRICE = 2.00

order_price = puzzle_volume * PUZZLE_PRICE + \
              dolls_volume * DOLL_PRICE + \
              bears_volume * BEAR_PRICE + \
              minions_volume * MINION_PRICE + \
              trucks_volume * TRUCK_PRICE

order_volume = puzzle_volume + dolls_volume + bears_volume + minions_volume + trucks_volume

if order_volume >= 50:
    bonus = order_price * 0.25
total_price = order_price - bonus

rent = total_price * 0.1

free_money = total_price - rent

net_money = free_money - vacation_price

if free_money >= vacation_price:
    print(f"Yes! {net_money:.2f} lv left.")
else:
    print(f"Not enough money! {vacation_price - free_money:.2f} lv needed.")