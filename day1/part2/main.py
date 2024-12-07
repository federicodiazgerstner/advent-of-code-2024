# Open the file
with open('input.txt', 'r') as file:
    column1 = []
    column2 = []
    totalSimilarityScore = 0

    # Read each line in the file
    for line in file:
        # Strip newline and split by whitespace (space or tab)
        numbers = line.split()
        column1.append(int(numbers[0]))
        column2.append(int(numbers[1]))

    column1.sort()
    column2.sort()

    for i in range(len(column1)):
        timesAppeared = 0
        for j in range(len(column2)):
            if column1[i] == column2[j]:
                timesAppeared += 1
        totalSimilarityScore += column1[i] * timesAppeared
    
    print(totalSimilarityScore)
