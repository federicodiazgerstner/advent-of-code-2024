def find_starting_position(map):
    for row in range(len(map)):
        for column in range(len(map[row])):
            if map[row][column] == "^":
                return [row, column]

def determine_next_position(row, column, direction, value):
    if direction == "up":
        if value == "." or value == "X" or value == "^":
            return [row - 1, column]
        else:
            return [row - 1, column + 1]
    elif direction == "right":
        if value == "." or value == "X" or value == "^":
            return [row, column + 1]
        else:
            return [row + 1, column + 1]
    elif direction == "down":
        if value == "." or value == "X" or value == "^":
            return [row + 1, column]
        else:
            return [row + 1, column - 1]
    else:
        if value == "." or value == "X" or value == "^":
            return [row, column - 1]
        else:
            return [row - 1, column - 1]

distinctPositions = 0
with open('input.txt', 'r') as file:
    text = file.read()
    map = text.splitlines()
    row, column = find_starting_position(map)
    isOutOfMap = False
    direction = "up"
    visitedPositions = []

    while not isOutOfMap:
        print(f"row: {row} | column: {column} | len(map): {len(map)} | len(map[column]): {len(map[column])} | direction: {direction}")
        if row > len(map) or row < 0 or column < 0 or column > len(map[column]):
            isOutOfMap = True
            break

        if map[row][column] == "." or map[row][column] == "^":
            if [row, column] not in visitedPositions:
                visitedPositions.append([row, column])
                distinctPositions += 1
        elif map[row][column] == "#":
            if direction == "up":
                direction = "right"
            elif direction == "right":
                direction = "down"
            elif direction == "down":
                direction = "left"
            else:
                direction = "up"
        
        row, column = determine_next_position(row, column, direction, map[row][column])
    
    print(f"Total distinct positions: {distinctPositions}")