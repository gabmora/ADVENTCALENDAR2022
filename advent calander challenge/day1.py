#import library to read file 
# count number of calories carried by each elf 
# find which elf carries the most calories 

#import library to read .txt file 
#create initial sum 
#if value before the space are bigger -- most calories

f = open(r"C:\Users\gabmoral\advent calander challenge\day1.txt")
contents = f.read()

lst = contents.split('\n')

largestAmountofCalories = 0 #max
largestAmountofCalories2 = 0 #elf w 2nd greatest calories
largestAmountofCalories3 = 0 #elf w 3rd greatest calories 
currentElfTotal = 0 #count

# traverse every  string in lst
for item in lst:
    if item == '':
        currentElfTotal = 0 #resets the count 
    else:
        num = int(item)
        currentElfTotal += num

    if currentElfTotal > largestAmountofCalories:
        largestAmountofCalories = currentElfTotal
    elif currentElfTotal > largestAmountofCalories2:
        largestAmountofCalories2 = currentElfTotal
    elif currentElfTotal > largestAmountofCalories3:
        largestAmountofCalories3 = currentElfTotal

print("Number of largest calories carrired by elf:" ,largestAmountofCalories)
print("Number of second largest calories carrired by elf:" ,largestAmountofCalories2)
print("Number of third calories carrired by elf:" ,largestAmountofCalories3)

total = largestAmountofCalories + largestAmountofCalories2 + largestAmountofCalories3

print("Total number of calories carried by top 3 elves:" , total)

