# Open the file
with open('input.txt', 'r') as file:
    column1 = []
    column2 = []
    totalresult = 0

    # Read each line in the file
    for line in file:
        # Strip newline and split by whitespace (space or tab)
        numbers = line.split()
        column1.append(int(numbers[0]))
        column2.append(int(numbers[1]))

    column1.sort()
    column2.sort()

    for i in range(len(column1)):
        totalresult += abs(column1[i] - column2[i])
    
    print(totalresult)
