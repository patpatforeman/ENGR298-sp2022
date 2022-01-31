import random


# copy in Dr. Forsyth's random list function for use
def generate_random_int_list(max_length, upper_bound):
    # generate random length between 2 and max_length
    list_length = int(random.uniform(2, max_length))

    # given the length above, sample the Natural Numbers up to upper_bound that many times
    vars = random.sample(range(upper_bound), list_length)

    # return the generated list
    return vars


# generate two random lists of integers
max_length = 20
upper_bound = 100
nums = generate_random_int_list(max_length, upper_bound)

# scan the list nums and place odds and evens in different lists
odds = list()
evens = list()

### YOUR CODE HERE ###

print("Odds: ", odds)
print("Evens: ", evens)
