import math


def calculate_pi(target_error):
    """ Implementation of Gauss–Legendre algorithm to approximate PI from https://en.wikipedia.org/wiki/Gauss%E2%80%93Legendre_algorithm

        :param target_error: Desired error for PI estimation
        :return: Approximation of PI to specified error bound
        """

    # initialize all the algorithm constants
    a = 1
    b = 1 / (2 ** (1 / 2))
    t = 1 / 4
    p = 1

    # keep track of current approximation and error
    approx = 0
    current_error = 100

    # loop while your current error is larger than the target
    while abs(current_error) > target_error:
        # calculate next state variables
        a_n = ((a + b) / 2)
        b_n = ((b * a) ** (1 / 2))
        t_n = t - p * ((a - a_n) ** 2)
        p_n = (2 * p)

        # calculate approximation
        approx = ((a_n + b_n) ** 2) / (4 * t_n)

        # update state variables for the next iteration
        a = a_n
        b = b_n
        t = t_n
        p = p_n

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
