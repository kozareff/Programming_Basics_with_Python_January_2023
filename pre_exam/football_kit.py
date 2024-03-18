tshirt_price = float(input())
goal_budget = float(input())

shorts_price = tshirt_price * 0.75
socks_price = shorts_price * 0.2
sneakers_price = (tshirt_price + shorts_price) * 2

total_sum = tshirt_price + shorts_price + socks_price + sneakers_price
bonus_sum = total_sum * 0.85

diff = abs(bonus_sum - goal_budget)

if bonus_sum > goal_budget:
    print(f'Yes, he will earn the world-cup replica ball!')
    print(f'His sum is {bonus_sum:.2f} lv.')

if bonus_sum < goal_budget:
    print(f'No, he will not earn the world-cup replica ball.')
    print(f'He needs {diff:.2f} lv. more.')