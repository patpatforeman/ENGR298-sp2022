import os
import time
from ekg_testbench import EKGTestBench
from student_qrs_solution import main as student_main


if __name__ == "__main__":

    # set to true if you wish to print overall stats to the screen
    print_debug = True

    # manually search data/ekg folder for CSV files as data
    # and txt files with annotations
    directory = "../data/ekg/challenge/"
    directory_path = os.path.dirname(directory)

    databases = list()
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.endswith(".csv"):
                databases.append(file.split(".")[0])

    annotation_files = [x + "_annotations.txt" for x in databases]

    # hold all results in a list
    results = list()

    for database, annot in zip(databases, annotation_files):
        # load the test bench with annotations
        annotation_path = directory + annot

        start_parse_annotations = time.time()
        tb = EKGTestBench(annotation_path)

        # check to see if annotations could be loaded
        if tb is None:
            continue

        # print("\t Parsing ",abs(time.time()-start_parse_annotations))

        # call the student main function which returns peaks
        data_path = directory + database + ".csv"

        start_ekg_detection = time.time()
        (signal, peaks) = student_main(data_path)
        # print("\t EKG Detection: ",abs(time.time()-start_ekg_detection))

        # calculate basic stats
        start_stat_calculation = time.time()

        # matched is a list of (peak, annotation) pairs; unmatched is a list of peaks that were
        # not matched to any annotation; and remaining is annotations that were not matched.
        peaks_list = peaks.tolist()
        (matched, unmatched, remaining) = tb.generate_stats(peaks_list)

        # if was matched, then is true positive
        true_positive = len(matched)

        # if response was unmatched, then is false positive
        false_positive = len(unmatched)

        # whatever remains in annotations is a missed detection
        false_negative = len(remaining)

        # print("\t Stat Calculation: ",abs(time.time()-start_stat_calculation))

        # calculate f1 score
        f1 = true_positive / (true_positive + 0.5 * (false_positive + false_negative))

        # throw all the results in a list so we can pretty print a table later
        results.append((database, true_positive, false_positive, false_negative, f1))

    if print_debug:
        tp_sum = 0
        fp_sum = 0
        fn_sum = 0

        print("-------------------------------------------------")
        print("Database|\t\tTP|\t\tFP|\t\tFN|\t\tF1")
        for (database, true_positive, false_positive, false_negative, f1) in results:
            print(database, "|\t\t", true_positive, "|\t", false_positive, '|\t', false_negative, '|\t', round(f1, 3))
            tp_sum += true_positive
            fp_sum += false_positive
            fn_sum += false_negative
        print("-------------------------------------------------")

        overall_F1 = tp_sum / (tp_sum + 0.5 * (fp_sum + fn_sum))
        print("\nOverall F1 Score:", round(overall_F1, 3))
