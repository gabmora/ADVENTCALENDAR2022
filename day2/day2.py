with open ('day2.txt') as file:
    rounds = [i for i in file.read().strip().split("\n")]

#print(rounds)

'''
A X = rock
B  Y= paper
C  Z= scissors
all possible outcomes:

A vs X = DRAW = (1 + 3) = 4
A vs Y = WIN = (2 + 6) = 8
A vs Z = LOSS = (3 + 0) = 3
B vs X = LOSS = (1 + 0) = 1
B vs Y = DRAW = (2 + 3) = 5
B vs Z = WIN = (3 + 6) = 9
C vs X = WIN = (1 + 6) = 7
C vs Y = LOSS = (2 + 0) = 2
C vs Z = DRAW = (3 + 3) = 6

'''
#create the DICTIONARY  of possible outcomes
outcomes = {
    "A X": 4, "A Y": 8, "A Z": 3, 
    "B X": 1, "B Y": 5, "B Z": 9,
    "C X": 7, "C Y": 2, "C Z": 6
}

total_points_p1 = 0 
for  round in rounds:
    total_points_p1 += outcomes[round]

print(total_points_p1)

desired_outcomes = {
    "A X": 3, "A Y": 4, "A Z": 8, 
    "B X": 1, "B Y": 5, "B Z": 9,
    "C X": 2, "C Y": 6, "C Z": 7
}

total_points_p2 = 0 
for  round in rounds:
    total_points_p2 += desired_outcomes[round]

print(total_points_p2)
