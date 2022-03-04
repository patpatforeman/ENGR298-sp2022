# bring in randomness cause we need it in our lives
import random


# copy in Dr. Forsyth's random list function for use
def generate_random_int_list(max_length, upper_bound):
    # generate random length between 2 and max_length
    list_length = int(random.uniform(2, max_length))

    # given the length above, sample the Natural Numbers up to upper_bound that many times
    random_vars = random.sample(range(upper_bound), list_length)

    # return the generated list
    return random_vars


def main(random_list):
    """
    Given a random list of integers, return two lists of only even and odd values from that random list
    :param random_list: A random list
    :return: A tuple containing (even , odd) list
    """
    # lists to hold the even and odd numbers
    # do not modify their names
    evens_list = []
    odds_list = []

    for i in nums:
        if i % 2 == 0:
            evens_list.append(i)
        else:
            odds_list.append(i)


    # do not modify this line
    return (evens_list, odds_list)


if __name__ == "__main__":
    # generate two random lists of integers
    max_length = 20
    upper_bound = 100
    nums = generate_random_int_list(max_length, upper_bound)

    # pass the random list to the student main
    (even, odd) = main(nums)

    # print out the list and see the results
    print("You were passed the list: ", nums)
    print("Here are all the evens: ", even)
    print("Here are all the odds: ", odd)
