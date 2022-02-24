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
for obj in data:
    if obj.county == 'Harrisonburg city' or 'Rockingham':
        cases_list.append(int(obj.cases))
print('The greatest number of new daily cases recorded was ' + str(max(cases_list)) + '.')

# write code to address the following question:
# In terms of absolute number of cases, when was the worst seven-day period in the city/county for new COVID cases?


# write code to address the following question:
# In terms of absolute number of cases, when was the rise in cases the fastest over a rolling week window?
# Over what period was the rise in cases the greatest

