locations = int(input())
mined_gold = 0
average_gold = 0

for _ in range(0, locations):
    expected_gold = float(input())
    days = int(input())
    for _ in range(0, days):
        mined_gold += float(input())

    average_gold = round(mined_gold / days, 2)
    if average_gold >= expected_gold:
        print(f"Good job! Average gold per day: {average_gold:.2f}.")
        mined_gold = 0
        average_mined_gold = 0
    else:
        print(f"You need {expected_gold - average_gold:.2f} gold.")
        mined_gold = 0
        average_mined_gold = 0