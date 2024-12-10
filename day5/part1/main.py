def is_update_valid(rules, update):
    for i in range(len(update)):
        for j in range(len(update)):
            if i == j: continue
            applyingRules = [rules for rules in rules if update[i] in rules and update[j] in rules]
            for rule in applyingRules:
                firstNumber = update[i] if i < j else update[j]
                secondNumber = update[j] if i < j else update[i]
                if rule[0] != firstNumber and rule[1] != secondNumber:
                    return False
    return True

total_sum_middle = 0

with open('input.txt', 'r') as file:
    fulltext = file.read()
    rulestext, seriestext = fulltext.split('\n\n')
    rulesstring = [line.split("|") for line in rulestext.splitlines()]
    rules = [[int(x), int(y)] for x, y in rulesstring]
    series = [list(map(int, line.split(","))) for line in seriestext.splitlines()]
    for update in series:
        if is_update_valid(rules, update):
            middle_page = update[len(update) // 2]
            total_sum_middle += middle_page

print(total_sum_middle)
