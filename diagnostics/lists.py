from util import generate_random_int_list


# Diagnostic #1: Complete the methods: student_min, student_max, and runner_up

# write a function to determine the minimum value in the list
# Don't use the min() function. That's too easy :)
def student_min(nums):

    min_student = nums[0]
    for i in nums:
        if i < min_student:
            min_student = i
    return min_student


# write a function to determine the maximum value in the list
# Don't use the max() function. That's too easy :)
def student_max(nums):

    max_student = nums[0]
    for i in nums:
        if i > max_student:
            max_student = i

    return max_student


# write a function that determines the 2nd highest value in the list. Not #1, but the runner up :)
def runner_up(nums):

    max_student = nums[0]
    for i in nums:
        if i > max_student:
            max_student = i

    run_up = nums[0]
    for i in nums:
        if run_up < i < max_student:
            run_up = i

    return run_up


if __name__ == "__main__":
    print('Welcome to the program!')

    print('Now generating a random length list of random integers....')
    rands = generate_random_int_list(10, 100)

    print('Random List is:')
    print(rands)

    print('Now running your code to determine the minimum value...')
    print('Maximum value is ' + str(student_max(rands)))
    print('Minimum value is ' + str(student_min(rands)))
    print('Second Highest value is ' + str(runner_up(rands)))

    print('All done!')
