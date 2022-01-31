import random
import numpy as np


# copy in Dr. Forsyth's random list function for use
def generate_random_int_list(list_length, upper_bound):
    # given the length above, sample the Natural Numbers up to upper_bound that many times
    randoms = random.sample(range(upper_bound), list_length)

    # return the generated list
    return randoms


# Part 1: Do this with a vector of known length
# create 2x 3-element vectors
a = [3, 1, -2, 7, 0]
b = [9, 2, 4, 0, 8]

### YOUR CODE HERE ###

# result should be 21
print(dot_product)

# Part 2: Now, deal with arrays of unknown length
max_length = 1000
maximum_value = 1000000
fixed_length = int(random.uniform(2, max_length))
a = generate_random_int_list(fixed_length, maximum_value)
b = generate_random_int_list(fixed_length, maximum_value)

# student code
dot_product = 0

### YOUR CODE HERE ###

# check code with numpy...
a_np = np.asarray(a)
b_np = np.asarray(b)

# use dot product from numpy to check this result
correct = np.dot(a_np,b_np)
error = correct-dot_product

# compare results
print("Your result: ", dot_product)
print("Correct result: ",correct)
print("Error: ",error)
