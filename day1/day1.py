f = open(r"day1\day1.txt")
contents = f.read()

lst = contents.split('\n')

largestAmountofCalories = 0 #max
largestAmountofCalories2 = 0 #elf w 2nd greatest calories
largestAmountofCalories3 = 0 #elf w 3rd greatest calories 
currentElfTotal = 0 #count

totals = []

# traverse every  string in lst
for item in lst:
    if item == '':
        totals.append(currentElfTotal)
        currentElfTotal = 0 #resets the count 
    else:
        num = int(item)
        currentElfTotal += num
    totals.sort(reverse=True)
    #print(totals)

    if currentElfTotal > largestAmountofCalories:
        largestAmountofCalories = currentElfTotal
    elif currentElfTotal > largestAmountofCalories2:
        largestAmountofCalories2 = currentElfTotal
    elif currentElfTotal > largestAmountofCalories3:
        largestAmountofCalories3 = currentElfTotal

print("Number of largest calories carrired by elf:" ,totals[0])
print("Number of second largest calories carrired by elf:" ,totals[1])
print("Number of third calories carrired by elf:" ,totals[2])

total = totals[0]+totals[1]+totals[2]

print("Total number of calories carried by top 3 elves:" , total)