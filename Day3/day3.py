data = open('input.txt', 'r')
rucksacks = data.read().split('\n')

test = ['vJrwpWtwJgWrhcsFMMfFFhFp',
        'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL',
        'PmmdzqPrVvPwwTWBwg',
        'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn',
        'ttgJtRGJQctTZtZT',
        'CrZsJsPPZsGzwwsLwLmpwMDw']

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

# for rucksack in rucksacks:
#     split_sack = len(rucksack)//2
#     compartment_1 = set(rucksack[:split_sack])
#     compartment_2 = rucksack[split_sack:]

#     for item in compartment_2:
#         if item in compartment_1:
#             TOTAL += priority_values_dict[item]
#             break
    

# PART 2 CORRECT ⭐️

def make_groups(rucksacks):
    GROUPS = []
    group_beg = 0
    group_end = 2
    while group_end < len(rucksacks):
        GROUPS.append(rucksacks[group_beg:group_end+1])
        group_beg = group_end+1
        group_end += 3
    
    return GROUPS

elf_groups = make_groups(rucksacks)

for group in elf_groups:
    sack_1 = set(group[0])
    sack_2 = set(group[1])
    for item in group[2]:
        if item in sack_1 and item in sack_2:
            TOTAL += priority_values_dict[item]
            break