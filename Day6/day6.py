data = open('input.txt', 'r')
characters = data.read().split('\n')

#PART 1 CORRECT ⭐️
marker = 0

for i in range(len(characters[0])-1):
    check = set(characters[0][i:i+4])
    if len(check) == 4 and marker >= 4:
        marker+=4
        break
    else:
        marker += 1

    
print(marker)