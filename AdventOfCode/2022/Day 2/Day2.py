import numpy as np
import pandas as pd

# Read the input.txt into data frame that is space delimited
df = pd.read_csv('input.txt', sep=' ', header=None)

# Add headers to the data frame
df.columns = ['Opponent', 'User']


# Remap the X->A, Y->B, Z->C in the User column
df['User'] = df['User'].map({'X': 'A', 'Y': 'B', 'Z': 'C'})

# Point for selection of user
userSelectionPoints = {'A': 1, 'B': 2, 'C': 3}

# Make a third column with the points for the user selection
df['UserPoints'] = df['User'].map(userSelectionPoints)

# Make a fourth column to determine if the user won, lost, or drew
# A = Rock, B = Paper, C = Scissors
# 0 points for losing, 3 points for drawing, 6 points for winning
df['Result'] = 0

playResults = {
    'A': {'A': 3, 'B': 0, 'C': 6},
    'B': {'A': 6, 'B': 3, 'C': 0},
    'C': {'A': 0, 'B': 6, 'C': 3}
}

# Create a Result column given the User and Opponent columns
df['Result'] = df.apply(lambda row: playResults[row['User']][row['Opponent']], axis=1)


# Make third column for final points
df['FinalPoints'] = df['UserPoints'] + df['Result']

# Get the sum total of the final points
totalPoints = df['FinalPoints'].sum()

# Print the total points
print(f'The total points that would be given by following the strategy is {totalPoints}')



# Remap the X->A, Y->B, Z->C back to original in the User column
df['User'] = df['User'].map({'A': 'X', 'B': 'Y', 'C': 'Z'})

# Rename User to NeededMove
df.rename(columns={'User': 'NeededMove'}, inplace=True)

# X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win
neededMove = {
    'X': {'A': 'C', 'B': 'A', 'C': 'B'},
    'Y': {'A': 'A', 'B': 'B', 'C': 'C'},
    'Z': {'A': 'B', 'B': 'C', 'C': 'A'}
}

# Create a NeededMove column given the User and Opponent columns
df['NeededMove'] = df.apply(lambda row: neededMove[row['NeededMove']][row['Opponent']], axis=1)


# Recalculate UserPoints given the NeededMove into a new column
df['UserPoints2'] = df['NeededMove'].map(userSelectionPoints)

# Recalculate Result given the NeededMove into a new column
df['Result2'] = df.apply(lambda row: playResults[row['NeededMove']][row['Opponent']], axis=1)


# Recalculate FinalPoints given the NeededMove into a new column
df['FinalPoints2'] = df['UserPoints2'] + df['Result2']


# Get the sum total of the final points
totalPoints2 = df['FinalPoints2'].sum()

# Print the total points
print(f'The total points that would be given by following the strategy is {totalPoints2}')