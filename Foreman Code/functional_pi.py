import math

def calculate_pi():


# main (body) here to call your function. Do not modify below this line
desired_error = 1E-10

approximation = calculate_pi(desired_error)

print("Solution returned PI=", approximation)

error = abs(math.pi - approximation)

if error < abs(desired_error):
    print("Solution is acceptable")
else:
    print("Solution is not acceptable")