from math import pi

type_of_the_figute = input()

result = 0

if type_of_the_figute == "square":
    side = float(input())

elif type_of_the_figute == "rectangle":
    first_side = float(input())
    second_side = float(input())
    result = first_side * second_side

elif type_of_the_figute == "circle":
    radius = float(input())
    result = pi * (radius ** 2)

elif type_of_the_figute == "triangle":
    side = float(input())
    height = float(input())
    result = side * height / 2

print(f"{result:.3f}")
