chicken_menu = int(input())
fish_menu = int(input())
vegan_menu = int(input())

chicken_menu_price = 10.35
fish_menu_price = 12.4
vegan_menu_price = 8.15
delivery_cost = 2.5

chicken_cost = chicken_menu * chicken_menu_price
fish_cost = fish_menu * fish_menu_price
vegan_cost = vegan_menu * vegan_menu_price
menus_cost = chicken_cost + fish_cost + vegan_cost
desert_price = menus_cost * 0.2
whole_price = menus_cost + desert_price + delivery_cost

print(whole_price)
