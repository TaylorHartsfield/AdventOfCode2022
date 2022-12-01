data = open('input.txt', 'r')
values = data.read().split('\n')


# PART 1 CORRECT ⭐️
most_calories = 0
counting = 0

for value in values:
    if not value:
        most_calories = max(counting, most_calories)
        counting = 0
    else:
        counting += int(value)


# PART 2 CORRECT ⭐️

all_calorie_counts = []
counting = 0

for value in values:
    if not value:
        all_calorie_counts.append(counting)
        counting = 0
    else:
        counting += int(value)

max_count = max(all_calorie_counts)
all_calorie_counts.remove(max_count)

next_count = max(all_calorie_counts)
all_calorie_counts.remove(next_count)

final_count = max(all_calorie_counts)
all_calorie_counts.remove(final_count)

print(max_count+next_count+final_count)


