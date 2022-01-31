# create a tuple contain various elements
t = (3, 1, 5, -1, 7)

# get length of tuple
print(len(t))

# tuple is iterable
for element in t:
    print(element)

# attempt to sort the tuple; should error
t.sort()

# can create a tuple from other iterable objects
myList = list([9, 5, 3, 1])
t1 = tuple(myList)

# unlike list, cannot edit elements; should error
t1.pop()
