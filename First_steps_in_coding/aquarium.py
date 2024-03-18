length = int(input())
wide = int(input())
height = int(input())
percent = float(input()) / 100

volume = length * wide * height
volume_liters = volume * 0.001
percent_liters = volume_liters * percent
result = volume_liters - percent_liters

print(result)

