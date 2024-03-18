import math

price_per_gpu = int(input())
price_per_transitioner = int(input())
el_per_gpu = float(input())
profit_per_gpu = float(input())

GPU_QUANTITY = 13
TRANSITIONERS = 13

price_for_gpu = price_per_gpu * GPU_QUANTITY
price_transitioner = price_per_transitioner * TRANSITIONERS

total_sum = price_transitioner + price_for_gpu + 1000

net_profit_per_gpu = profit_per_gpu - el_per_gpu
net_profit_all = GPU_QUANTITY * net_profit_per_gpu

days_to_return = math.ceil(total_sum / net_profit_all)

print(total_sum)
print(days_to_return)