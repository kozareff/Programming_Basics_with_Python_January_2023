kg_dog = int(input())

kg_dog *= 1000

eaten_food_per_day = input()

while eaten_food_per_day != "Adopted":
    eaten_food = int(eaten_food_per_day)
    kg_dog -= eaten_food
    eaten_food_per_day = input()


if kg_dog  >= 0:
    print(f"Food is enough! Leftovers: {kg_dog} grams." )

else:
    print(f"Food is not enough. You need {abs(kg_dog)} grams more.")