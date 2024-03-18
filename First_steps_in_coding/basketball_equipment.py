tax_per_year = int(input())

snickers = tax_per_year * 0.6
jersey = snickers * 0.8
ball = jersey / 4
accessories = ball / 5

whole_price = tax_per_year + snickers + jersey + ball + accessories

print (f'{whole_price:.2f}')



