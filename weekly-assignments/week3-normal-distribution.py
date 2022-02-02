import numpy as np

# parameters for distribution and samples to generate
mu = 0
std = 1
num_samples = 10

# use normal to generate distribution samples

# use mean() to determine the average of those samples
mean = -1

# use std() to determine the standard deviation of samples
deviation = -1

# check if sufficient samples were taken. Do not modify below this line
print("mu=", mean, "stdev=", deviation)

deviation_error = abs(1 - deviation)

if mean < 1E-3 and deviation_error < 1E-3:
    print('Solution within error tolerances')
else:
    print('Solution is not within error tolerances')
