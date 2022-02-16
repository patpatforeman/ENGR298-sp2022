import numpy as np
import matplotlib.pyplot as plt

# sample a signal at a give rate (Hz)
sample_rate = 1000

# determine the sample period
period = 1/sample_rate

# over 10s, sample the signal
time = np.arange(0,10,period)

# generate a sine wave of frequency (Hz)
freq = 20
sine = np.sin(2*np.pi*time)

# use matplotlib to plot sine wave
plt.plot(time,sine)

# label the x and y axis
plt.xlabel("Time (s)")
plt.ylabel("Signal Amplitude")

# provide a nice title
plt.title("Plot of a "+str(freq)+" Hz Sine Wave")

# now show the plot
plt.show()
