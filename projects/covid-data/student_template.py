from file_utils import load_with_pickle
from covid_point import CovidRecord
import numpy as np
import pandas as pd

# load covid data as list of CovidRecord objects
data = load_with_pickle('covid_data.pickle')

# Create lists to hold the data
hburg_cases = list()
rockingham_cases = list()
hburg_dates = list()

# Loops to Pull Data from Pickle
for obj in data:
    if obj.county == 'Rockingham':
        rockingham_cases.append(int(obj.cases))
    if obj.county == 'Harrisonburg city':
        hburg_cases.append(int(obj.cases))
        hburg_dates.append(obj.date)  # From inspection, Harrisonburg has the first recorded case date

# Add in zero Values to make both cases lists the same length
for z in range(9):
    rockingham_cases.insert(0, 0)

# Add the two case lists together to make one data set
total_cases = list(np.add(rockingham_cases, hburg_cases))

# When was the first positive COVID case in Rockingham County and Harrisonburg?

first_positive = list()
i = 0

# Iterate through list of cases, assign dates to cases, then append to list
for obj in range(len(total_cases)):
    if i > len(total_cases):  # Breakout Condition so Python doesn't yell at me
        break
    if total_cases[i] > 0:
        first_positive.append(hburg_dates[i])
    i += 1

# Print out Results from first problem
print('The first recorded case in The Harrisonburg/Rockingham'
      ' county area was ' + first_positive[0] + '.')

# What day was the greatest number of new daily cases recorded in Harrisonburg and Rockingham County?
i = 0
start = 0

# Use For Loop to find Max new case value
for obj in range(len(total_cases)):
    if i >= len(total_cases) - 1:  # Breakout Condition, you betcha
        break
    if total_cases[i + 1] - total_cases[i] > start:
        start = total_cases[i + 1] - total_cases[i]  # Start holds new Max Case Value
        max_case = hburg_dates[i]  # Day of Max Case
        min_case = hburg_dates[i - 1]  # Day before Max Case
    i += 1

# Print out 2nd problem Results
print('The greatest number of new daily cases recorded was ' + str(start) + ', which happened going from ' +
      min_case + ' to ' + max_case + '.')

# In terms of absolute number of cases, when was the worst seven-day period in the city/county for new COVID cases?
a = 0
b = 6
begin = 0
worst_last = 0

# Complicated For Loop
for obj in range(len(total_cases)):
    if b >= len(total_cases) - 1:  # Breakout Baby
        break
    worst_first = (total_cases[a] + total_cases[a + 1] + total_cases[a + 2] + total_cases[a + 3]
        + total_cases[a + 4] + total_cases[a + 5] + total_cases[b])
    if (worst_first - total_cases[b]) / 7 > begin:
        begin = (worst_first - total_cases[b]) / 7  # Begin Holds the sum of cases
        worst_start = hburg_dates[a]
        worst_end = hburg_dates[b]
    worst_last = worst_first
    a += 1
    b += 1

print('The worst week for absolute number of cases was the week from ' + worst_start + ' to '
      + worst_end +', with a total number of ' + str(begin) + ' cases.')

# Over what period was the rise in cases the greatest?
n = 0
m = 6
start = 0
for obj in range(len(total_cases)):
    if m >= len(total_cases):
        break
    start_roll = total_cases[n]
    end_roll = total_cases[m]
    if end_roll - start_roll > start:
        start = end_roll - start_roll
        roll_fin = hburg_dates[m]
        roll_start = hburg_dates[n]
    n += 1
    m += 1

print('The greatest rise in cases was ' + str(start) + ' cases, which occurred during the week from ' +
      roll_start + ' to ' + roll_fin + '.')



