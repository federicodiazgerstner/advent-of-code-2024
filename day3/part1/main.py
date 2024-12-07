import re

total = 0
with open('input.txt', 'r') as file:
    text = ""
    for line in file:
        text += line

    pattern = r"mul\((\d{1,3}),\s*(\d{1,3})\)"
    do = "do()"
    dont = "don't()"
    currentString = ""
    enabled = True
    for i in range(len(text)):
        if enabled:
            occurrences = re.findall(pattern, currentString)
            if(len(occurrences) > 0):
                total += int(occurrences[0][0]) * int(occurrences[0][1])
                currentString = ""
        currentString += text[i]

        isEnabled = currentString.find(do)
        isDisabled = currentString.find(dont)
        if(isEnabled != -1): 
            enabled = True
            currentString = ""
        if(isDisabled != -1): 
            enabled = False
            currentString = ""

print(total)