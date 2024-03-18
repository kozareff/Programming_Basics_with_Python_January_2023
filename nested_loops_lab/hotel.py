number_of_floors = int(input())
flats_per_floor = int(input())

flat_name = ''
flat_number = 0

for current_floor in range(number_of_floors, 0, -1):
    for number in range(flats_per_floor):

        if current_floor == number_of_floors:
            flat_name = f'L{current_floor}{number}'
        elif current_floor % 2 == 0:
            flat_name = f'O{current_floor}{number}'
        elif current_floor % 2 != 0:
            flat_name = f'A{current_floor}{number}'

        print(flat_name, end=' ')
    print()