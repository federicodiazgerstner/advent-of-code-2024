# G = {i+j*1j: c for i,r in enumerate(open('input.txt'))
#                for j,c in enumerate(r.strip())}

# start = min(p for p in G if G[p] == '^')

# def walk(G):
#     pos, dir, seen = start, -1, set()
#     while pos in G and (pos,dir) not in seen:
#         seen |= {(pos,dir)}
#         if G.get(pos+dir) == "#":
#             dir *= -1j
#         else: pos += dir
#     return {p for p,_ in seen}, (pos,dir) in seen

# path = walk(G)[0]
# print(len(path),
#       sum(walk(G | {o: '#'})[1] for o in path))

def find_starting_position(map):
    for row in range(len(map)):
        for column in range(len(map[row])):
            if map[row][column] == "^":
                return [row, column]

def determine_next_position(map, row, column, direction, obsRow, obsCol):
    if direction == "up":
        if row - 1 < 0:
            return [row - 1, column, direction]
        if map[row - 1][column] == "#" or (row - 1 == obsRow and column == obsCol):
            return [row, column + 1, "right"]
        else:
            return [row - 1, column, "up"]
    elif direction == "right":
        if column + 1 >= len(map[row]):
            return [row, column + 1, direction]
        if map[row][column + 1] == "#" or (row == obsRow and column + 1 == obsCol):
            return [row + 1, column, "down"]
        else:
            return [row, column + 1, "right"]
    elif direction == "down":
        if row + 1 >= len(map):
            return [row + 1, column, direction]
        if map[row + 1][column] == "#" or (row + 1 == obsRow and column == obsCol):
            return [row, column - 1, "left"]
        else:
            return [row + 1, column, "down"]
    else:
        if column - 1 < 0:
            return [row, column - 1, direction]
        if map[row][column - 1] == "#" or (row == obsRow and column - 1 == obsCol):
            return [row - 1, column, "up"]
        else:
            return [row, column - 1, "left"]

def simulate_guard(map, obstruction):
    row, column = find_starting_position(map)
    direction = "up"
    visited = set()
    while True:
        if row > len(map) or row < 0 or column < 0 or column > len(map[0]):
            return False  # Guard exited the map
        visited.add((row, column, direction))
        row, column, direction = determine_next_position(map, row, column, direction, *obstruction)
        if (row, column, direction) in visited:
            return True  # Loop detected
        

def find_obstruction_positions(map, visitedPositions):
    start_row, start_col = find_starting_position(map)
    possible_positions = 0
    for position in visitedPositions:
            row, column = position
            if [row, column] == [start_row, start_col] or map[row][column] == "#":
                continue
            if simulate_guard(map, (row, column)):
                possible_positions += 1
    return possible_positions

distinctPositions = 0
with open('input.txt', 'r') as file:
    text = file.read()
    map = text.splitlines()
    row, column = find_starting_position(map)
    isOutOfMap = False
    direction = "up"
    visitedPositions = []

    while not isOutOfMap:
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
        
        row, column, direction = determine_next_position(map, row, column, direction, row, column)
    
    result = find_obstruction_positions(map, visitedPositions)
    print(result)
    