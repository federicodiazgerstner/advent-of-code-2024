def is_ordered(rules, update):
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
def fix_update(rules, update):
    fixedArray = update
    ordered = False
    while not ordered:
        for i in range(len(fixedArray)):
            for j in range(len(fixedArray)):
                firstNumber = fixedArray[i] if i < j else fixedArray[j]
                secondNumber = fixedArray[j] if i < j else fixedArray[i]
                applyingRules = [rules for rules in rules if rules[0] == firstNumber and rules[1] == secondNumber]
                if len(applyingRules) == 0:
                    previousNumber = fixedArray[i]
                    fixedArray[i] = fixedArray[j]
                    fixedArray[j] = previousNumber
            ordered = is_ordered(rules, fixedArray)
    return fixedArray[len(fixedArray)// 2]

def check_and_fix_updates(rules, update):
    if is_ordered(rules, update):
        return 0
    else:
        return fix_update(rules, update)

total_sum_middle = 0

with open('input.txt', 'r') as file:
    fulltext = file.read()
    rulestext, seriestext = fulltext.split('\n\n')
    rulesstring = [line.split("|") for line in rulestext.splitlines()]
    rules = [[int(x), int(y)] for x, y in rulesstring]
    series = [list(map(int, line.split(","))) for line in seriestext.splitlines()]
    for update in series:
        total_sum_middle += check_and_fix_updates(rules,update)

print(total_sum_middle)
