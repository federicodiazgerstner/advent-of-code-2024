# Open the file
with open('input.txt', 'r') as file:
    numberOfSafeReports = 0

    for report in file:
        levels = report.split()
        if (all(int(levels[i]) < int(levels[i + 1]) for i in range(0, len(levels)-1)) or all(int(levels[i]) > int(levels[i + 1]) for i in range(0, len(levels)-1))):
            if(all(1 <=abs(int(levels[i]) - int(levels[i + 1])) <= 3 for i in range(0, len(levels)-1))):
                numberOfSafeReports += 1
    print(numberOfSafeReports)
