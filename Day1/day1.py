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

print(most_calories)



