totalOccurrences = 0
with open('input.txt', 'r') as file:
#with open('test.txt', 'r') as file:
    text = file.read()
    lines = text.splitlines()
    for line in range(len(lines)):
        for letter in range(len(lines[line])):
            if(lines[line][letter] == "X"):
                #find reverse
                reversed = ""
                if(letter >= 3):
                    reversed = lines[line][letter] + lines[line][letter - 1] + lines[line][letter - 2] + lines[line][letter - 3]
                    if reversed == "XMAS": 
                        totalOccurrences += 1
                        print(f"Found reversed from X in pos ({line + 1},{letter + 1})")
                #find horizontal
                next = ""
                if(len(lines[line]) - letter > 3):
                    next = lines[line][letter] + lines[line][letter + 1] + lines[line][letter + 2] + lines[line][letter + 3]
                    if next == "XMAS": 
                        totalOccurrences += 1
                        print(f"Found next from X in pos ({line + 1},{letter + 1})")
                #find vertical
                verticalUp = ""
                if(line >= 3):
                    verticalUp = lines[line][letter] + lines[line - 1][letter] + lines[line - 2][letter] + lines[line - 3][letter]
                    if verticalUp == "XMAS": 
                        totalOccurrences += 1
                        print(f"Found vertical UP from X in pos ({line + 1},{letter + 1})")
                verticalDown = ""
                if(len(lines) - line > 3):
                    verticalDown = lines[line][letter] + lines[line + 1][letter] + lines[line + 2][letter] + lines[line + 3][letter]
                    if verticalDown == "XMAS": 
                        totalOccurrences += 1
                        print(f"Found verticalDown from X in pos ({line + 1},{letter + 1})")
                #find diagonal SE
                diagonalSE = ""
                if (len(lines) - line > 3 and len(lines[line]) - letter > 3):
                    diagonalSE = lines[line][letter] + lines[line + 1][letter + 1] + lines[line + 2][letter + 2] + lines[line + 3][letter + 3]
                    if(diagonalSE == "XMAS"): 
                        totalOccurrences += 1
                        print(f"Found diagonalSE from X in pos ({line + 1},{letter + 1})")

                diagonalNE = ""
                if (line >= 3 and len(lines[line]) - letter > 3):
                    diagonalNE = lines[line][letter] + lines[line - 1][letter + 1] + lines[line - 2][letter + 2] + lines[line - 3][letter + 3]
                    if(diagonalNE == "XMAS"): 
                        totalOccurrences += 1
                        print(f"Found diagonalNE from X in pos ({line + 1},{letter + 1})")
                
                diagonalNW = ""
                if (line >= 3 and letter >= 3):
                    diagonalNW = lines[line][letter] + lines[line - 1][letter - 1] + lines[line - 2][letter - 2] + lines[line - 3][letter - 3]
                    if(diagonalNW == "XMAS"): 
                        totalOccurrences += 1
                        print(f"Found diagonalNW from X in pos ({line + 1},{letter + 1})")
                
                diagonalSW = ""
                if (len(lines) - line > 3 and letter >= 3):
                    diagonalSW = lines[line][letter] + lines[line + 1][letter - 1] + lines[line + 2][letter - 2] + lines[line + 3][letter - 3]
                    if(diagonalSW == "XMAS"): 
                        totalOccurrences += 1
                        print(f"Found diagonalSW from X in pos ({line + 1},{letter + 1})")



print(totalOccurrences)
