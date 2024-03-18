month = input()
number_of_nights = int(input())

price_studio = 0
price_apartment = 0

if month == 'May' or month == 'October':
    price_studio = number_of_nights * 50
    price_apartment = number_of_nights * 65

    if 7 < number_of_nights <= 14:
        price_studio *= 0.95

    elif number_of_nights > 14:
        price_studio *= 0.70

elif month == 'June' or month == 'September':
    price_studio = number_of_nights * 75.20
    price_apartment = number_of_nights * 68.70

    if number_of_nights > 14:
        price_studio *= 0.80

elif month == 'July' or month == 'August':
    price_studio = number_of_nights * 76
    price_apartment = number_of_nights * 77

if number_of_nights > 14:
    price_apartment *= 0.90

print(f'Apartment: {price_apartment:.2f} lv.')
print(f'Studio: {price_studio:.2f} lv.')