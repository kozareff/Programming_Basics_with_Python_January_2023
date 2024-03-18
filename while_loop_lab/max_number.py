current_number = int(input())

while True:
    user_input = input()
    if user_input == 'Stop':
        break
    num = int(user_input)
    if num > current_number:
        current_number = num

print(current_number)