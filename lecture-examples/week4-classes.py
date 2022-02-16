# directly declare a list
declared_list = [1, 2, 3, 4]

# call the list constructor to create the list
constructed_list = list()

# use the list class method extend() to copy the lists
constructed_list.extend(declared_list)

if declared_list == constructed_list:
    print("Lists are the same!")
else:
    print("Lists are not the same!")


# create a basic class to represent points
# yes, we can do this in the middle of the program because this is Python
class Point:
    # give the class some default values
    x = 0
    y = 0

    # my stuff list
    my_stuff = []


# Instantiate a new Point A and set values to (1,1)
a = Point()
a.x = 1
a.y = 1
print("Point A contains", a.x, a.y)

# now make B. See what it's default value is
b = Point()
print("Point B contains", b.x, b.y)

# give A some objects, should stay with A
a.my_stuff.append("10 bitcoins")
print("A has", a.my_stuff)

# B shouldn't have anything, right?
print("B has", b.my_stuff)


# A corrected point class that utilizes the constructor to create local variables
class PointCorrect:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.my_stuff = []


# Instantiate a new Point A and set values to (1,1)
a = PointCorrect()
a.x = 1
a.y = 1
print("Point A contains", a.x, a.y)

# now make B. See what it's default value is
b = PointCorrect()
print("Point B contains", b.x, b.y)

# give A some objects, should stay with A
a.my_stuff.append("10 bitcoins")
print("A has", a.my_stuff)

# B shouldn't have anything, right?
print("B has", b.my_stuff)


# An implementation of point class that has two constructors
class PointClassConstructed:

    # advanced constructor with initial parameters and
    # now with default values
    def __init__(self, _x=0, _y=0):
        self.x = _x
        self.y = _y
        self.my_stuff = []


# Instantiate a new Point A and set values to (1,1)
a = PointClassConstructed(1, 1)
print("Point A contains", a.x, a.y)

# now make B. See what it's default value is
b = PointClassConstructed()
print("Point B contains", b.x, b.y)

