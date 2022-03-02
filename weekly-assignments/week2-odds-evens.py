# bring in randomness cause we need it in our lives
import random


# copy in Dr. Forsyth's random list function for use
def generate_random_int_list(max_length, upper_bound):
    # generate random length between 2 and max_length
    list_length = int(random.uniform(2, max_length))

    # given the length above, sample the Natural Numbers up to upper_bound that many times
    vars = random.sample(range(upper_bound), list_length)

    # return the generated list
    return vars


def main(random_list):
    # variable to hold the odd or even count
    # do not modify their names
    num_even = 0
    num_odd = 0

    ###### Your code begins here #####

    # do not modify this line
    return (num_even, num_odd)


if __name__ == "__main__":
    # generate two random lists of integers
    max_length = 20
    upper_bound = 100
    nums = generate_random_int_list(max_length, upper_bound)

    # pass the random list to the student main
    (odd, even) = main(nums)

    # print out the list and see the results
    print("You were sent the list: ", nums)
    print("Your solution reported ", odd, " odd values and ", even, "even values.")
