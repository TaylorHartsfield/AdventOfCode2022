data = open('input.txt', 'r')
pairs = data.read().split('\n')

test = ['2-4,6-8',
        '2-3,4-5',
        '5-7,7-9',
        '2-8,3-7',
        '6-6,4-6',
        '2-6,4-8']


#PART 1 CORRECT ⭐️
OVERLAP_SECTIONS = 0

for sections in pairs:
    sections.split(',')
    split_sections = sections.split(',')
    elf_1_sections = split_sections[0].split('-')
    elf_2_sections = split_sections[1].split('-')
    
    # min_section = min(int(elf_1_sections[0]), int(elf_2_sections[0]))
    # max_section = max(int(elf_1_sections[1]), int(elf_2_sections[1]))

   
    # if (min_section == int(elf_1_sections[0]) and max_section == int(elf_1_sections[1])) or\
    # (min_section == int(elf_2_sections[0]) and max_section == int(elf_2_sections[1])):
    #     OVERLAP_SECTIONS += 1


# PART 2 CORRECT ⭐️ (Comment out line 21-27 to run part 2 and vice versa)

    full_range = range(int(elf_1_sections[0]), int(elf_1_sections[1])+1)
    for val in range(int(elf_2_sections[0]), int(elf_2_sections[1])+1):
        if val in full_range:
            OVERLAP_SECTIONS+=1
            break
  
    
