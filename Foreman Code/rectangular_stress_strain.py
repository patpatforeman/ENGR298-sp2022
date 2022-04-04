import numpy as np
import os
import math
import sys

def parse_tensile_file(path_to_file):
    file = open(path_to_file)
    # required meta-data
    width = -1
    thickness = - 1
    length = -1
    # determine when to begin reading into these files
    begin_reading = False
    time = []
    extension = []
    load = []
    # begin iterating through file
    for line in file:
        if line == '' or line == '\n':
            continue

        splits = line.strip().split(",")

        if begin_reading == False:

            # gather various meta data
            if splits[0] == "Width":
                cleaned = splits[1].replace('\"', '')
                width = float(cleaned)
            if splits[0] == "Thickness":
                cleaned = splits[1].replace('\"', '')
                thickness = float(cleaned)
            if splits[0] == "Length":
                cleaned = splits[1].replace('\"', '')
                length = float(cleaned)

        else:
            # parse the actual data
            time.append(float(splits[0].replace('\"', '')))
            extension.append(float(splits[1].replace('\"', '')))
            load.append(float(splits[2].replace('\"', '')))

        # try to find start of data
        if splits[0] == "(s)":
            begin_reading = True
    file.close()

    return width, thickness, length, np.asarray(time), np.asarray(extension), np.asarray(load)

def calculate_stress(width, thickness, load):
    """
    Calculate the stress (MPa) experienced by the test given a series of forces/loads (kN) and
    a sample diameter (mm)
    :param force: An array of forces/loads applied to the sample in Kilo Newtons (kN)
    :param sample_diameter: The diameter of the sample in millimeters (mm)
    :return: An array of stresses experienced by the sample in Kilo Pascals (KPa)
    """

    # calculate the cross-section area (from mm to in^s)
    area = (thickness * 0.0393701) * (width * 0.0393701)

    # delete this line and replace it with your own
    stress = (load * 0.224809) / area

    return stress

def calculate_strain(extension, length):
    strain = (extension * 0.0393701) / (length * 0.0393701)

    return strain


def calculate_max_strength_strain(strain, stress):
    """
    Calculate the Ultimate Tensile Stress and Fracture Strain
    :param strain: An array of Strain data (MPa)
    :param stress: An array of Strain data
    :return:
    Ultimate Tensile Stress: the maximum stress experienced
    Fracture Strain: the maximum strain experienced before fracture
    """

    # calculate the maximum stress experienced
    ultimate_tensile_stress = max(stress)

    # calculate the maximum strain experienced
    fracture_strain = max(strain)

    return ultimate_tensile_stress, fracture_strain


def calculate_elastic_modulus(strain, stress):
    """
    Given a set of stress strain data, use the Secant Modulus at 40% method to determine
    the elastic modulus
    :param strain: An array of Strain data (MPa)
    :param stress: An array of Strain data
    :return:
    linear_index: the index within the strain/stress data that is the end of the linear region
    slope: the slope for the linear region of the strain/stress data
    intercept: y-intercept for linear region best fit of strain/stress data
    """

    # dummy variables to check that the values are implemented. These should be over-written by your
    # code throughout this method
    linear_index = -1
    slope = -1
    intercept = -1

    # Step 3a: find the point that is 40% of max strain
    # replace the line below with your code to find the secant_strain
    secant_stress = (max(stress) * 0.4)

    # Step 3b: find the index closes to that 40%
    # take the diff of the whole array and use argmin to find the index where the closest
    # value occurs

    # uncomment the line below and find the difference between stress and secant across all values
    diffs = np.abs(stress - secant_stress)

    # uncomment the line below and use np.argmin on the diffs array to find the index/location of the closest point
    linear_index = np.argmin(diffs)

    # Step 3c: down select to linear region for stress and strain using array slicing
    # uncomment the lines below and use array slicing to select points between 0 and the linear index
    linear_stress = stress[0:linear_index]
    linear_strain = strain[0:linear_index]

    # Step 3d: find least squares fit to a line in the linear region
    # use 1-degree polynominal fit (line)
    # uncomment the line below and use np.polyfit to determine a best fit for the linear stress/strain regions
    slope, intercept = np.polyfit(linear_strain, linear_stress, 1)

    return linear_index, slope, intercept

if __name__ == "__main__":
    import matplotlib.pyplot as plt

    # modify this line to select different materials/folders within tensile/
    material_folder = "Materials Data"

    # modify this line to select different samples in the material folder
    sample_name = "LCS_1"

    ### Do not modify below this line ###

    path_to_directory = "../Foreman Code/"
    path_to_samples = path_to_directory + material_folder + "/"

    # manually parse file to get gage diameter and then calculate cross-sectional area
    path_to_file = path_to_samples + sample_name + ".csv"

    # Step #1: Parse the file ane return based values
    # sample diameter (mm), time (s), displacement (mm), force (kN), and strain (%)
    width, thickness, length, time, extension, load = parse_tensile_file(path_to_file)

    stress = calculate_stress(width, thickness, load)
    strain = calculate_strain(extension, length)

    # use scatter plot so we don't assume a line (yet)
    plt.scatter(strain, stress, label="Stress - Strain")
    plt.xlabel('Strain (in/in)')
    plt.ylabel('Stress (psi)')
    plt.title('Stress-Strain Curve for Sample ' + sample_name)
    plt.show()

# Step #2: Calculate basic parameters such as the ultimate tensile strength
    # and fracture strain

    # calculate easy variables
    ultimate_tensile_strength, fracture_strain = calculate_max_strength_strain(strain, stress)

    if ultimate_tensile_strength==-1 or fracture_strain ==-1:
        print("Error! Tensile Strength or Fracture Strain returned as -1. Did you complete the calculate_max_strength() method?")
        sys.exit(-1)

    print("Ultimate Tensile Stress is ", ultimate_tensile_strength, "psi")
    print("Fracture Strain is ", 100 * fracture_strain, " percent")

    # Step #3: Use the Secant Modulus at 40% of Peak Strain
    # to determine elastic modulus

    linear_index, slope, intercept = calculate_elastic_modulus(strain, stress)

    if linear_index==-1 or slope==-1 or intercept ==-1:
        print("Error! You did not calculate the linear region or index correctly. Check the calculate_elastic_modulus() method.")
        sys.exit(-1)

    print("Elastic Modulus is ", slope, 'psi')

    # show the original curve indicating the secant modulus at 40%
    plt.scatter(strain, stress, label="Stress - Strain")
    plt.xlabel('Strain (%)')
    plt.ylabel('Stress (MPa)')
    plt.title('Stress-Strain Curve for Sample ' + sample_name)

    plt.scatter(strain[linear_index], stress[linear_index], marker="v", label="Secant Modulus at 40%")

    plt.legend()
    plt.show()

    # now plot the linear region for the best fit line
    linear_strain = strain[0:linear_index]
    linear_stress = stress[0:linear_index]

    plt.scatter(linear_strain, linear_stress, label="Stress - Strain")
    plt.xlabel('Strain (%)')
    plt.ylabel('Stress (MPa)')
    plt.title('Linear Region for Sample ' + sample_name + ' with best fit')

    # compute line y=mx+b
    best_fit_line = slope * linear_strain + intercept
    plt.plot(linear_strain, best_fit_line, label="Best Linear Fit")

    plt.legend()
    plt.show()
