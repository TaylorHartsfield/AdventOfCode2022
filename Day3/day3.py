data = open('input.txt', 'r')
rucksacks = data.read().split('\n')


# PART 1 CORRECT ⭐️
LOWER = "abcdefghijklmnopqrstuvwxyz"
UPPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
TOTAL = 0

def make_priority_dict(LOWER, UPPER):

    priority_values = {}
    value = 1

    for letter in LOWER:
        priority_values[letter] = value
        value += 1
    
    for letter in UPPER:
        priority_values[letter] = value
        value += 1
    
    return priority_values
    
priority_values_dict = make_priority_dict(LOWER, UPPER)

for rucksack in rucksacks:
    split_sack = len(rucksack)//2
    compartment_1 = set(rucksack[:split_sack])
    compartment_2 = rucksack[split_sack:]

    for item in compartment_2:
        if item in compartment_1:
            TOTAL += priority_values_dict[item]
            break
    

