deposit_amount = float(input())
months = int(input())
annual_rate = float(input())

per_year = deposit_amount * (annual_rate / 100)
per_month = per_year / 12
total_sum = deposit_amount + (per_month * months)

print(total_sum)

