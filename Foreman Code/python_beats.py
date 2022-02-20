
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

# use matplot lib to generate a single

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(a, c, color='pink', linewidth=1)
ax.plot(a, b, color='lightblue', linewidth=1)
plt.xlim([0, 10])
ax.set(title='EKG Data',
       ylabel='Voltage (mV)',
       xlabel='Time (s)')
plt.show()
