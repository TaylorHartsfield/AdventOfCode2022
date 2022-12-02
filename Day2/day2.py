"""
A - Rock
B - Paper
C - Scissors

X - Rock - 1pt
Y - Paper - 2pt
Z - Scissors - 3pt

LOST - 0pt
DRAW - 3pt
WIN - 6pt
"""

# PART 1 CORRECT ⭐️

data = open('input.txt', 'r')
games = data.read().split('\n')


POINTS = {
    "A X": 4,
    "A Y": 8,
    "A Z": 3,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 7,
    "C Y": 2,
    "C Z": 6
}

total_score = 0

for game in games:
    total_score += POINTS[game]


print(total_score)


#PART 2 CORRECT ⭐️

"""
A - Rock
B - Paper
C - Scissors

X - lose
Y - draw
z - win

Rock - 1pt
Paper - 2pt
Scissors - 3pt

LOST - 0pt
DRAW - 3pt
WIN - 6pt

"""
OUTCOME_POINTS = {
    "A X": 3,
    "A Y": 4,
    "A Z": 8,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 2,
    "C Y": 6,
    "C Z": 7
}

total_outcome_score = 0

for game in games:
    total_outcome_score += OUTCOME_POINTS[game]


print(total_outcome_score)

