percent_fat = int(input())
percent_protein = int(input())
percent_vagle = int(input())
calories = int(input())
percent_water = int(input()) / 100

calories_per_gram_fat = 9
calories_per_gram_protein = 4
calories_per_gram_vagle = 4

total_grams_fat = ((calories * percent_fat ) / calories_per_gram_fat) / 100
total_grams_protein = ((calories * percent_protein ) / calories_per_gram_protein) / 100
total_grams_vagle = ((calories * percent_vagle ) / calories_per_gram_vagle) / 100

total_weight_food = total_grams_vagle + total_grams_protein + total_grams_fat
calories_per_gram_food = calories / total_weight_food
calories_per_gram_food_with_water = calories_per_gram_food - (calories_per_gram_food * percent_water)

print (f'{calories_per_gram_food_with_water:.4f}')
