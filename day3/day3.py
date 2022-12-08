from string import ascii_letters

with open (r'C:\Users\gabmoral\OneDrive - Capgemini\Documents\advent calander challenge\day3\day3.txt') as f:
    contents = [i for i in f.read().strip().split("\n")]
    #print(contents)
    #iterate through rucksack

totalSum = 0
for rucksack in contents:
    half = len(rucksack)//2 #find half (//2  --> sets as int not double)

    left = set(rucksack[:half])
    right = set(rucksack[half:])
        #print(rucksack, left, right)

    for priority, char in enumerate(ascii_letters): # assign every letter a number 
        #print(priority, char)
        if char in left and char in right:
            totalSum += priority + 1

print("answer to part 1:", totalSum) 
#part 2: find common char in rucksacks
j = 3
totalSum = 0
for i in range(0, len(contents), 3):
    rucksacks = contents[i:j]
    j += 3
    
    for priority, char in enumerate(ascii_letters): # assign every letter a number 
        #print(priority, char)                       3enumerate stars at 0
        if char in rucksacks[0] and char in rucksacks[1] and char in rucksacks[2]:
            totalSum += priority + 1
print("answer to part 2:", totalSum)
            