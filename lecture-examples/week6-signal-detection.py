import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

# load saved data from numpy array
filepath = '../data/ekg/processed_mitdb_201.npy'

# once loaded, place in an array called filtered
filtered = np.load(filepath)

# plot the first ~10s to see what we have..
signal = filtered[0:3300]
plt.plot(signal)
plt.title('Filtered Data')
# plt.show()

# Method 1: Use Simple Threshold with Timeout

# set a detection threshold
detection_threshold = 2.0

# set a heart beat time out
detection_time_out = 50

# track the last time we found a beat
last_detected_index = -1

# keep not of where we are in the data
current_index = 0

# store indices of all found beats
beats_detected = list()

# loop through signal finding beats
for value in signal:

    # if current value is greater than threshold AND it has been
    # long enough since our previous heart beat detection
    if value > detection_threshold \
            and abs(current_index - last_detected_index) > detection_time_out:
        # update the last time we found a beat
        last_detected_index = current_index

        # add this index to the list of our beats
        beats_detected.append(current_index)

    # update our current index
    current_index += 1

print("Within the sample we found ", len(beats_detected), " heart beats with manual search!")

beats_detected = np.asarray(beats_detected)

plt.plot(beats_detected, signal[beats_detected], 'X')
# plt.show()

# Method 2: Use Find Peaks
peaks, _ = find_peaks(signal, distance=100, height=1)
print("Within the sample we found ", len(peaks), " heart beats with find_peaks!")

# plot all the find_peaks results on the same graph
plt.plot(peaks, signal[peaks], 'p')
plt.show()
