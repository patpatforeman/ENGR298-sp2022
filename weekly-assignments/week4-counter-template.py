import random


class Counter:
    """
    A simple counter class with initialization and inc/dec operations
    """

    def __init__(self, _init=0):
        """
        Initial the counter. Default value is 0

        :param _init: Initial counter value
        """
        self.count = ...

    def dec(self):
        """
        Decrement the count by 1

        :return: None
        """
        # decrement self.count
        ### your code here ###
        return None

    def inc(self):
        """
        Increment the count by 1

        :return: None
        """
        # increment self.count
        ### your code here ###
        return None

    def get_count(self):
        """
        Get the current value of the counter

        :return: Current value of the counter
        """
        # return the value of self.count
        ### your code here ###
        return None


### Main program begins here... ###
if __name__ == "__main__":

    # create a counter. Increment the value 5x times. Result should be 5.
    my_counter = Counter()
    my_counter.inc()
    my_counter.inc()
    my_counter.inc()
    my_counter.inc()
    my_counter.inc()

    print("Counter is ", my_counter.get_count())

    # decrement the counter 3x times. Result should be 2
    my_counter.dec()
    my_counter.dec()
    my_counter.dec()

    print("Counter is ", my_counter.get_count())

    # create a new counter and initialize to a random value
    initial_value = random.randint(0, 100)
    random_counter = Counter(initial_value)

    # check to see that the initial value was set correctly
    if random_counter.get_count() == initial_value:
        print("Constructor implemented correctly!")
    else:
        print("Error in constructor implementation. Counter value should be ", initial_value)

    # now decrement a random number of times. Save the before and after value
    # so we can double check to see if operation was performed successfully.
    num_to_decrement = random.randint(0, 100)
    before = random_counter.get_count()

    # do a bunch of decrement operations!
    for i in range(0, num_to_decrement):
        random_counter.dec()

    # calculate correct result
    correct = before - num_to_decrement

    if random_counter.get_count() == correct:
        print("Decrement implemented correctly!")
    else:
        print("Error in decrement implementation.")
        print("Result is ", random_counter.get_count(), " Should be: ", correct)

    # now increment a random number of times. Save the before and after value
    # so we can double check to see if operation was performed successfully.
    num_to_increment = random.randint(0, 100)
    before = random_counter.get_count()

    # do a bunch of decrement operations!
    for i in range(0, num_to_increment):
        random_counter.inc()

    # calculate correct result
    correct = before + num_to_increment

    if random_counter.get_count() == correct:
        print("Increment implemented correctly!")
    else:
        print("Error in increment implementation.")
        print("Result is ", random_counter.get_count(), " Should be: ", correct)
