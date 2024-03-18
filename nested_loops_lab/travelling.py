while True:
    destination = input()
    if destination == 'End':
        break

    budged = float(input())
    saved_money = 0

    while destination != 'End':
        saved_money += float(input())
        if saved_money >= budged:
            print(f'Going to {destination}!')
            break