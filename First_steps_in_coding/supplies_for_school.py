pen_count = int(input())
marker_count = int(input())
detergent_liter = int(input())
discount_percent = int(input()) / 100

price_pen = 5.8
price_marker = 7.2
price_detergent = 1.2

total_price_pen = price_pen * pen_count
total_price_markekrs = price_marker * marker_count
total_price_detergent = price_detergent * detergent_liter

price_supplies = total_price_pen + total_price_markekrs + total_price_detergent
price_with_discount = price_supplies - (price_supplies * discount_percent)

print(price_with_discount)