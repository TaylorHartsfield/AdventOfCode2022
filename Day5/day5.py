data = open('input.txt', 'r')
moves = data.read().split('\n')

#PART 1 CORRECT ⭐️
stacks = {
    "stack1":["N","R","G","P"],
    "stack2":["J","T","B","L","F","G","D","C"],
    "stack3":["M","S","V"],
    "stack4":["L","S","R","C","Z","P"],
    "stack5":["P","S","L","V","C","W","D","Q"],
    "stack6":["C","T","N","W","D","M","S"],
    "stack7":["H","D","G","W","P"],
    "stack8":["Z","L","P","H","S","C","M","V"],
    "stack9":["R","P","F","L","W","G","Z"]
    }

for move in moves:
    new_move = move.split(' ')
    num = int(new_move[1])
    from_stack = new_move[3]
    to_stack= new_move[5]
    
    i = 1
    while i <= num:
        move = stacks[f'stack{from_stack}'].pop()
        stacks[f'stack{to_stack}'].append(move)
        i+= 1

print(stacks)

