
import matplotlib.pyplot as plt
import numpy as np

# import the CSV file using numpy
path = '../data/ekg/mitdb_201.csv'

# load data in matrix from CSV file; skip first two rows
ekg_data = np.loadtxt(path, skiprows=2, delimiter=',')

# save each vector as own variable
a = np.array(ekg_data[:, 0])
b = np.array(ekg_data[:, 1])
c = np.array(ekg_data[:, 2])


# pass data through LOW PASS FILTER (OPTIONAL)
## your code here

# pass data through HIGH PASS FILTER (OPTIONAL) to create BAND PASS result
## your code here


# pass data through differentiator
diff_b = np.diff(b)
diff_c = np.diff(c)

difference_b = np.insert(diff_b, [0], [0])
difference_c = np.insert(diff_c, [0], [0])

# pass data through square function
square_b = np.square(difference_b)
square_c = np.square(difference_c)

# pass through moving average window
mov_avgb = np.convolve(square_b, 1)
mov_avgc = np.convolve(square_c, 1)

# use matplotlib to generate figures for each intermediate signal
# you may wish to example the sampling rate for your selected file
# to determine how many points for each vector to plot

# Differential Plot
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(a, difference_b, color='lightblue', linewidth=1)
ax.plot(a, difference_c, color='pink', linewidth=1)
plt.xlim([0, 10])
ax.set(title='EKG Data Differentiated',
       ylabel='Voltage (mV)',
       xlabel='Time (s)')
plt.show()

# Square Plot
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(a, square_b, color='lightblue', linewidth=1)
ax.plot(a, square_c, color='pink', linewidth=1)
plt.xlim([0, 10])
ax.set(title='EKG Data Squared',
       ylabel='Voltage (mV)',
       xlabel='Time (s)')
plt.show()

# Final Plot
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(a, mov_avgc, color='pink', linewidth=1)
ax.plot(a, mov_avgb, color='lightblue', linewidth=1)
plt.xlim([0, 10])
ax.set(title='EKG Data Moving Average',
       ylabel='Voltage (mV)',
       xlabel='Time (s)')
plt.show()

