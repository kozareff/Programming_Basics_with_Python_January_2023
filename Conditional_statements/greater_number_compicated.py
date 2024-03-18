first_number = int(input())
second_number = int(input())
if first_number > second_number:
    print(f"{first_number} is greater than {second_number}")
elif second_number > first_number:
    print(f"{second_number} is greater than {first_number}")
elif first_number == second_number:
    print(f"{first_number} and {second_number} are equal")
