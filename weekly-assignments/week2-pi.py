import math


def main():
    """
    Use the Gauss-Legendre Algorithm to estimate Pi. Perform 10 approximation loops. Once complete, return the approximation.
    :return:
    """


    ### Your code here ###



    # set pi_estimate to whatever variable you were using for pi
    pi_estimate = ...

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
