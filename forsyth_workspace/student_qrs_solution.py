import numpy as np
from scipy.signal import find_peaks, butter, lfilter
from ekg_testbench import EKGTestBench
import statistics

def main(filepath):
    if filepath == '':
        return list()

    # import the CSV file using numpy
    path = filepath

    # load data in matrix from CSV file; skip first two rows
    ekg_data = np.loadtxt(path, skiprows=2, delimiter=',')

    # save each vector as own variable
    a = np.array(ekg_data[:, 0])
    b = np.array(ekg_data[:, 1])
    c = np.array(ekg_data[:, 2])

    # Bandpass Code
    def butter_bandpass(lowcut, highcut, fs, order=5):
        nyq = 0.5 * fs
        low = lowcut / nyq
        high = highcut / nyq
        m, n = butter(order, [low, high], btype='band')
        return m, n

    def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
        m, n = butter_bandpass(lowcut, highcut, fs, order=order)
        y = lfilter(m, n, data)
        return y

    # Bandpass Parameters
    fs = 5000.0
    lowcut = 100.0
    highcut = 1250.0

    filtered_c = butter_bandpass_filter(c, lowcut, highcut, fs)

    # pass data through differentiator
    diff_b = np.diff(b)
    diff_c = np.diff(filtered_c)

    difference_b = np.insert(diff_b, [0], [0])
    difference_c = np.insert(diff_c, [0], [0])

    # pass data through square function
    square_b = np.square(difference_b)
    square_c = np.square(difference_c)

    # pass through moving average window
    mov_avgb = np.convolve(square_b, 1)
    mov_avgc = np.convolve(square_c, 1)

    # take the output of the moving average and save it to 'signal' to it can be passed
    # back to the testbench
    signal = mov_avgc

    # use find_peaks to identify peaks within averaged/filtered data
    # save the peaks result and return as part of testbench result
    peaks, _ = find_peaks(mov_avgc, distance=137.9, height=(statistics.mean(signal)) * 2.42)
    # do not modify this line
    return signal, peaks


# when running this file directly, this will execute first
if __name__ == "__main__":
    import matplotlib.pyplot as plt
    # database name
    database_name = 'mitdb_219'

    # set to true if you wish to generate a debug file
    file_debug = False

    # set to true if you wish to print overall stats to the screen
    print_debug = True

    # set to true if you wish to show a plot of each detection process
    show_plot = False

    ### DO NOT MODIFY BELOW THIS LINE!!! ###

    # path to ekg folder
    path_to_folder = "../data/ekg/challenge/"

    # select a signal file to run
    signal_filepath = path_to_folder+database_name+".csv"

    # call main() and run against the file. Should return the filtered
    # signal and identified peaks
    (signal, peaks) = main(signal_filepath)

    # matched is a list of (peak, annotation) pairs; unmatched is a list of peaks that were
    # not matched to any annotation; and remaining is annotations that were not matched.
    annotation_path = path_to_folder+database_name+"_annotations.txt"
    tb = EKGTestBench(annotation_path)
    peaks_list = peaks.tolist()
    (matched, unmatched, remaining) = tb.generate_stats(peaks_list)

    # if was matched, then is true positive
    true_positive = len(matched)

    # if response was unmatched, then is false positive
    false_positive = len(unmatched)

    # whatever remains in annotations is a missed detection
    false_negative = len(remaining)

    # calculate f1 score
    f1 = true_positive / (true_positive + 0.5 * (false_positive + false_negative))

    # if we wish to show the resulting plot
    if show_plot:
        # make a nice plt of results
        plt.title('Signal for ' + database_name + " with detections")

        plt.plot(signal, label="Filtered Signal")
        plt.plot(peaks, signal[peaks], 'p', label='Detected Peaks')

        true_annotations = np.asarray(tb.annotation_indices)
        plt.plot(true_annotations, signal[true_annotations], 'o', label='True Annotations')

        plt.legend()

        # uncomment line to show the plot
        plt.show()

    # if we wish to save all the stats to a file
    if file_debug:
        # print out more complex stats to the debug file
        debug_file_path = database_name + "_debug_stats.txt"
        debug_file = open(debug_file_path, 'w')

        # print out indices of all false positives
        debug_file.writelines("-----False Positives Indices-----\n")
        for fp in unmatched:
            debug_file.writelines(str(fp) + "\n")

        # print out indices of all false negatives
        debug_file.writelines("-----False Negatives Indices-----\n")
        for fn in remaining:
            debug_file.writelines(str(fn.sample) + "\n")

        # close file that we writing
        debug_file.close()

    if print_debug:
        print("-------------------------------------------------")
        print("Database|\t\tTP|\t\tFP|\t\tFN|\t\tF1")
        print(database_name, "|\t\t", true_positive, "|\t", false_positive, '|\t', false_negative, '|\t', round(f1, 3))
        print("-------------------------------------------------")

    print("Done!")

