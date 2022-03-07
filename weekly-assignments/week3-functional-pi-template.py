import math


def calculate_pi(target_error):
    """ Implementation of Gauss–Legendre algorithm to approximate PI from https://en.wikipedia.org/wiki/Gauss%E2%80%93Legendre_algorithm

        :param target_error: Desired error for PI estimation
        :return: Approximation of PI to specified error bound
        """

    # initialize all the algorithm constants
    a = ### your code here ###
    b = ### your code here ###
    t = ### your code here ###
    p = ### your code here ###

    # keep track of current approximation and error
    approx = 0
    current_error = 100

    # loop while your current error is larger than the target
    while abs(current_error) > target_error:
        # calculate next state variables
        a_ = ### your code here ###
        b_ = ### your code here ###
        t_ = ### your code here ###
        p_ = ### your code here ###

        # calculate approximation
        approx = ### your code here ###

        # update state variables for the next iteration
        a = ### your code here ###
        b = ### your code here ###
        t = ### your code here ###
        p = ### your code here ###

        # determine error
        current_error = math.pi - approx

    return approx


if __name__ == "__main__":
    # main (body) here to call your function. Do not modify below this line
    desired_error = 1E-10

    approximation = calculate_pi(desired_error)

    print("Solution returned PI=", approximation)

    error = abs(math.pi - approximation)

    if error < abs(desired_error):
        print("Solution is acceptable")
    else:
        print("Solution is not acceptable")
