import random
import numpy as np


# copy in Dr. Forsyth's random list function for use
def generate_random_int_list(list_length, upper_bound):
    # given the length above, sample the Natural Numbers up to upper_bound that many times
    randoms = random.sample(range(upper_bound), list_length)

    # return the generated list
    return randoms


def dot_product(listA, listB):
    """
    Calculate the dot product of two lists containing integers
    :param listA: A list of integers
    :param listB: B list of integers
    :return: The dot product result (a1*b1)+(a2*b2)+(...,...)
    """
    if len(listA) != len(listB):
        print("Lists are two different lengths! You did something wrong!")

    # make a variable to hold the result from the dot product
    total = 0

    # loop through both lists and calculate the dot product
    for i in range(len(listA)):
        total += listA[i] * listB[i]

    # return the variable. Do not modify this line
    return total


if __name__ == "__main__":
    # Part 1: Do this with a vector of known length
    # create 2x 3-element vectors
    a = [3, 1, -2, 7, 0]
    b = [9, 2, 4, 0, 8]

    # calculate the dot product of two lists
    result = dot_product(a, b)

    # result should be 21
    print("Performing dot product of listA: ", a, " and listB: ", b)
    print("Result is: ", result)

    # Part 2: Now, deal with arrays of unknown length
    max_length = 10
    maximum_value = 100
    fixed_length = int(random.uniform(2, max_length))
    a = generate_random_int_list(fixed_length, maximum_value)
    b = generate_random_int_list(fixed_length, maximum_value)

    # calculate the dot product of two lists
    result = dot_product(a, b)

    # result should be 21
    print("Performing dot product of:)")
    print("List A:", a)
    print("List B:", b)

    # check code with numpy...
    a_np = np.asarray(a)
    b_np = np.asarray(b)

    # use dot product from numpy to check this result
    correct = np.dot(a_np, b_np)
    error = correct - result

    # compare results
    print("Your result: ", result)
    print("Correct result: ", correct)
    print("Error: ", error)
