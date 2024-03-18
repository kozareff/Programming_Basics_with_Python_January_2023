days = int(input()) - 1
typeroom = input()
review = input()

cost = 0

if typeroom == "room for one person":
    cost = days * 18


elif typeroom == "apartment":
    cost = days * 25
    if days < 10:
        cost *= 0.70
    elif 10 <= days <= 15:
        cost *= 0.65
    elif days > 15:
        cost *= 0.50


elif typeroom == "president apartment":
    cost = days * 35
    if days < 10:
        cost *= 0.90
    elif 10 <= days <= 15:
        cost *= 0.85
    elif days > 15:
        cost *= 0.80

if review == "positive":
    cost *= 1.25
elif review == "negative":
    cost *= 0.90

print(f'{cost:.2f}')