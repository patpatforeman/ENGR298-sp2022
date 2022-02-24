from file_utils import load_with_pickle
from covid_point import CovidRecord

# load covid data as list of CovidRecord objects
data = load_with_pickle('covid_data.pickle')


# write code to address the following question:
# When was the first positive COVID case in Rockingham County and Harrisonburg?
first_positive = list()
for obj in data:
    if obj.county == 'Harrisonburg city' or 'Rockingham' and obj.cases == '1':
        first_positive.append(obj.date)
print('The first recorded case in The Harrisonburg/Rockingham'
      ' county area was ' + first_positive[0] + '.')

# write code to address the following question:
# What day was the greatest number of new daily cases recorded in Harrisonburg and Rockingham County?
cases_list = list()
date_list = list()
for obj in data:
    if obj.county == 'Rockingham':
        cases_list.append(int(obj.cases))
        date_list.append(obj.date)
print('The greatest number of new daily cases recorded was ' + str(max(cases_list)) + '.')

# write code to address the following question:
# In terms of absolute number of cases, when was the worst seven-day period in the city/county for new COVID cases?
a = 0
b = 6
begin = 0
for obj in range(len(cases_list)):
    if b >= len(cases_list):
        break
    worst_period = sum(cases_list[:obj + b])
    if worst_period > begin:
        worst = worst_period
        worst_start = date_list[a]
        worst_end = date_list[b]
    a += 1
    b += 1

print('The worst week for absolute number of cases was the week from ' + worst_start + ' to '
      + worst_end +', with a total number of ' + str(worst) + ' cases.')

# write code to address the following question:
# In terms of absolute number of cases, when was the rise in cases the fastest over a rolling week window?
# Over what period was the rise in cases the greatest
n = 0
m = 6
start = 0
for obj in range(len(cases_list)):
    if m >= len(cases_list):
        break
    start_roll = cases_list[n]
    end_roll = cases_list[m]
    if end_roll - start_roll > start:
        start = end_roll - start_roll
        roll_fin = date_list[m]
        roll_start = date_list[n]
    n += 1
    m += 1

print('The greatest rise in cases was ' + str(start) + ' cases, which occurred during the week from ' +
      roll_start + ' to ' + roll_fin + '.')



