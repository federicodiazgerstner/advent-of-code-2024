def is_safe(levels):
    if (all(int(levels[i]) < int(levels[i + 1]) for i in range(0, len(levels)-1)) or all(int(levels[i]) > int(levels[i + 1]) for i in range(0, len(levels)-1))):
        if(all(1 <=abs(int(levels[i]) - int(levels[i + 1])) <= 3 for i in range(0, len(levels)-1))):
            return True
    return False

def is_safe_with_dampener(report):
    if is_safe(report.split()):
        return True
    
    levels = report.split()
    for i in range(len(levels)):
        modified_report = levels[:i] + levels[i+1:]  # Remove the i-th level
        if is_safe(modified_report):
            return True
    return False

with open('input.txt', 'r') as file:
    numberOfSafeReports = 0

    for report in file:
        if is_safe_with_dampener(report):
             numberOfSafeReports += 1
    print(numberOfSafeReports)
