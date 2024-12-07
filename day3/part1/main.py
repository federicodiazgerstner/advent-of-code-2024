import re

total = 0
with open('input.txt', 'r') as file:
    text = ""
    for line in file:
        text += line

    pattern = r"mul\((\d{1,3}),\s*(\d{1,3})\)"
    occurrences = re.findall(pattern, text)
    for occurrence in occurrences:
        total += int(occurrence[0]) * int(occurrence[1])

print(total)