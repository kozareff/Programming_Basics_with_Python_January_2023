first_index_max, second_index_max, third_index_max = int(input()), int(input()), int(input())

condition = False

for first_number in range(1, first_index_max + 1):

    for second_number in range(2, second_index_max + 1):
        condition = True
        for i in range(2, second_number):
            if second_number % i == 0:
                condition = False
        if not condition:
            continue
        else:
            second_number_prime = second_number

        for third_number in range(1, third_index_max + 1):

            if first_number % 2 == 0 and third_number % 2 == 0:
                print(f"{first_number} {second_number_prime} {third_number}")