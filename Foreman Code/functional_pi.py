import math

def calculate_pi(de):
    """
    Returns a value for 𝜋 within a certain error bound.

    :param de: Desired Error Limits for Generated Pi Value
    """
    # Set Initial Values
    a = 1
    b = 1 / (2 ** (1 / 2))
    t = 1 / 4
    p = 1
    approx = 0

    # Create a loop to iterate through until condition is met
    while True:
        a_n = ((a + b) / 2)
        b_n = ((b * a) ** (1 / 2))
        t_n = t - p * ((a - a_n) ** 2)
        p_n = (2 * p)

        # This Section gives me my pi approximation and the percent difference between my pi
        # and Python's pi
        approx = ((a_n + b_n) ** 2) / (4 * t_n)
        error = (abs((approx - math.pi) / math.pi)) * 100

        # This simply appends the initial values to the final values to increase accuracy through the loop
        a = a_n
        b = b_n
        t = t_n
        p = p_n

        # Breakout Condition
        if error > de or error == de:
            continue
        else:
            break
    return approx

# main (body) here to call your function. Do not modify below this line
desired_error = 1E-10


approximation = calculate_pi(desired_error)

print("Solution returned PI=", approximation)

error = abs(math.pi - approximation)

if error < abs(desired_error):
    print("Solution is acceptable")
else:
    print("Solution is not acceptable")
