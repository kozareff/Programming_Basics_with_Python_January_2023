text = input()

summary = 0

for i in text:
    if i == "a":
        summary += 1
    elif i == "e":
        summary += 2
    elif i == "i":
        summary += 3
    elif i == "o":
        summary += 4
    elif i == "u":
        summary += 5

print(summary)