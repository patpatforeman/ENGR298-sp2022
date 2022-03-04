import math


def main():
    """
    Use the Gauss-Legendre Algorithm to estimate Pi. Perform 10 approximation loops. Once complete, return the approximation.
    :return:
    """

    # Set Initial Values
    a = 1
    b = 1 / (2 ** (1 / 2))
    t = 1 / 4
    p = 1
    loop = range(1, 11)

    # Create a loop to iterate through ten times
    for i in loop:
        a_n = ((a + b) / 2)
        b_n = ((b * a) ** (1 / 2))
        t_n = t - p * ((a - a_n) ** 2)
        p_n = (2 * p)

        # This Section gives me my pi approximation and the percent difference between my pi
        # and Python's pi
        approx_pi = ((a_n + b_n) ** 2) / (4 * t_n)
        percent_diff = (abs((approx_pi - math.pi) / math.pi)) * 100

        # This simply appends the initial values to the final values to increase accuracy through the loop
        a = a_n
        b = b_n
        t = t_n
        p = p_n



    # set pi_estimate to whatever variable you were using for pi
    pi_estimate = approx_pi

    # return the estimated value of pi
    return pi_estimate


if __name__ == "__main__":

    # call the student function
    result = main()

    # print results
    error = abs(math.pi - result)

    # print out the results
    print("You returned the value: ", result)
    print("This has error of: ", error)
    if error < 1E-9:
        print("This is acceptable...")
    else:
        print("The error is too much. Are you looping 10 times?")
