totalOccurrences = 0
def is_xmas(string):
    return string == "MAS" or string == "SAM"

with open('input.txt', 'r') as file:
#with open('test.txt', 'r') as file:
    text = file.read()
    lines = text.splitlines()
    for line in range(1, len(lines) - 1):
        for letter in range(1, len(lines[line]) - 1):
            if lines[line][letter] == "A":
                text1 = lines[line - 1][letter - 1] + lines[line][letter] + lines[line + 1][letter + 1]
                text2 = lines[line + 1][letter - 1] + lines[line][letter] + lines[line - 1][letter + 1]
                if is_xmas(text1) and is_xmas(text2):
                    totalOccurrences += 1


                



print(totalOccurrences)
