import numpy as np

# Read in the calorieList.txt without line break
with open('calorieList.txt') as f:
    calorieList = f.read().splitlines()


##############################
# Part 1
##############################

elfCalorieList = []
temp = []
for i, val in enumerate(calorieList):
    if val == '':
        elfCalorieList.append(temp)
        temp = []
    elif i == len(calorieList) - 1:
        temp.append(int(val))
        elfCalorieList.append(temp)
    else:
        temp.append(int(val))


# Get the max of the sums of the sublists
individualCalorieSums = [sum(x) for x in elfCalorieList]
print(f'Max calorie of a single elf: {max(individualCalorieSums)}')


##############################
# Part 2
##############################

# Get the sum of the top three individual calorie sums
topThree = np.sort(individualCalorieSums)[-3:]
print(f'Top three calorie sums: {sum(topThree)}')


