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
