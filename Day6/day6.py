data = open('input.txt', 'r')
characters = data.read().split('\n')

#PART 1 CORRECT ⭐️
marker_one = 0

for i in range(len(characters[0])-1):
    check = set(characters[0][i:i+4])
    if len(check) == 4 and marker_one >= 4:
        marker_one+=4
        break
    else:
        marker_one += 1

#PART 2 Correct ⭐️
marker_two = 0

for i in range(len(characters[0])-1):
    check = set(characters[0][i:i+14])
    if len(check) == 14 and marker_two >= 14:
        marker_two += 14
        break
    else:
        marker_two += 1
    
print(marker_one, marker_two)