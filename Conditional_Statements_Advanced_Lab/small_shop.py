product = input()
city = input()
quantity = float(input())

price = 0

if city == 'Sofia':
        if product == 'coffee':
                total_sum = 0.5 * quantity
        elif product == 'water':
                total_sum = 0.8 * quantity
        elif product == 'beer':
                total_sum = 1.2 * quantity
        elif product == 'sweets':
                total_sum = 1.45 * quantity
        elif product == 'peanuts':
                total_sum = 1.6 * quantity

elif city == 'Plovdiv':
        if product == 'coffee':
                total_sum = 0.4 * quantity
        elif product == 'water':
                total_sum = 0.7 * quantity
        elif product == 'beer':
                total_sum = 1.15 * quantity
        elif product == 'sweets':
                total_sum = 1.3 * quantity
        elif product == 'peanuts':
                total_sum = 1.5 * quantity

elif city == 'Varna':
        if product == 'coffee':
                total_sum = 0.45 * quantity
        elif product == 'water':
                total_sum = 0.7 * quantity
        elif product == 'beer':
                total_sum = 1.1 * quantity
        elif product == 'sweets':
                total_sum = 1.35 * quantity
        elif product == 'peanuts':
                total_sum = 1.55 * quantity

print(total_sum)