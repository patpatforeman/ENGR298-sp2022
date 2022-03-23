import numpy as np
import os
import math


def parse_tensile_file(path_to_file):
    file = open(path_to_file)
    # required meta-data
    gage_diameter = -1
    maximum_force = - 1
    maximum_strain = -1
    # determine when to begin reading into these files
    begin_reading = False
    time = []
    displacement = []
    force = []
    strain = []
    # begin iterating through file
    for line in file:
        if line == '' or line == '\n':
            continue

        splits = line.strip().split(",")

        if begin_reading == False:

            # gather various meta data
            if splits[0] == "Gage Diameter":
                cleaned = splits[2].replace('\"', '')
                gage_diameter = float(cleaned)
            if splits[0] == "Maximum Force":
                cleaned = splits[2].replace('\"', '')
                maximum_force = float(cleaned)
            if splits[0] == "Maximum Strain":
                cleaned = splits[2].replace('\"', '')
                maximum_strain = float(cleaned)

        else:
            # parse the actual data
            time.append(float(splits[0].replace('\"', '')))
            displacement.append(float(splits[1].replace('\"', '')))
            force.append(float(splits[2].replace('\"', '')))
            strain.append(float(splits[3].replace('\"', '')))

        # try to find start of data
        if splits[0] == "(s)":
            begin_reading = True
    file.close()

    return gage_diameter, np.asarray(time), np.asarray(displacement), np.asarray(force), np.asarray(strain)


def calculate_stress(force, sample_diameter):
    """
    Calculate the stress (MPa) experienced by the test given a series of forces/loads (kN) and
    a sample diameter (mm)
    :param force: An array of forces/loads applied to the sample in Kilo Newtons (kN)
    :param sample_diameter: The diameter of the sample in millimeters (mm)
    :return: An array of stresses experienced by the sample in Kilo Pascals (KPa)
    """

    # calculate the cross-section area (mm^2)
    ### your code here ###

    # calculate stress (MPa) from load (kN) and cross-sectional area
    ### your code here ###

    return stress


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

    ### put your calculation where -1 is ###
    ultimate_tensile_stress = -1

    ### put your calculation where -1 is ###
    fracture_strain = -1

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

    # Step 3a: find the point that is 40% of max strain

    ### put your calculation where -1 is ###
    secant_strain = -1

    # Step 3b: find the index closes to that 40%
    # take the diff of the whole array and use argmin to find the index where the closest
    # value occurs

    ### your code below ###
    diffs = np.abs()

    ### your code below ###
    linear_index = np.argmin()

    # Step 3c: down select to linear region for stress and strain using array slicing

    ### put your calculation where -1 is ###
    linear_stress = -1

    ### put your calculation where -1 is ###
    linear_strain = -1

    # Step 3d: find least squares fit to a line in the linear region
    # use 1-degree polynominal fit (line)
    # replace 0 and 0 with approriate variables
    slope, intercept = np.polyfit(0,0, 1)

    return linear_index, slope, intercept


if __name__ == "__main__":
    import matplotlib.pyplot as plt

    # modify this line to select different materials/folders within tensile/
    material_folder = "1045CR"

    # modify this line to select different samples in the material folder
    sample_name = "C01A1045CR_1"


    ### Do not modify below this line ###

    path_to_directory = "../data/tensile/"
    path_to_samples = path_to_directory + material_folder + "/"

    # manually parse file to get gage diameter and then calculate cross-sectional area
    path_to_file = path_to_samples + sample_name + ".csv"

    # Step #1: Parse the file ane return based values
    # sample diameter (mm), time (s), displacement (mm), force (kN), and strain (%)
    sample_diameter, time, displacement, force, strain = parse_tensile_file(path_to_file)

    #plt.scatter(strain,force,label="Force - Strain")
    #plt.xlabel("Strain (%)")
    #plt.ylabel("Force (kN)")
    #plt.title("Force Applied and Resulting Strain")
    #plt.show()

    # Step #1: Given the forces and sample diameter, calculate the strain
    stress = calculate_stress(force, sample_diameter)

    # use scatter plot so we don't assume a line (yet)
    plt.scatter(strain, stress, label="Stress - Strain")
    plt.xlabel('Strain (%)')
    plt.ylabel('Stress (MPa)')
    plt.title('Stress-Strain Curve for Sample ' + sample_name)
    plt.show()

    # Step #2: Calculate basic parameters such as the ultimate tensile strength
    # and fracture strain

    # calculate easy variables
    ultimate_tensile_strength, fracture_strain = calculate_max_strength_strain(strain, stress)
    print("Ultimate Tensile Stress is ", ultimate_tensile_strength, "MPa")
    print("Fracture Strain is ", 100 * fracture_strain, " percent")

    # Step #3: Use the Secant Modulus at 40% of Peak Strain
    # to determine elastic modulus

    linear_index, slope, intercept = calculate_elastic_modulus(strain, stress)

    print("Elastic Modulus is ", slope / 1000, 'GPa')

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

    ##### calculate yield strength #####
    # https://professorkazarinoff.github.io/Engineering-Materials-Programming/07-Mechanical-Properties/calculate-yield-strength-programmatically.html

    # next to find point that intersects y=m(x-0.002) + 0
    offset = 0.002

    # calculate the offset line
    offset_line = slope * (strain - offset)

    # measure distance from all points on graph to this line
    distance = abs(stress - offset_line)
    intercept_index = np.argmin(distance)

    # create line parallel to linear region and find intersection with overall curve
    plt.scatter(strain, stress, label="Stress - Strain")
    plt.xlabel('Strain (%)')
    plt.ylabel('Stress (MPa)')
    plt.title('Stress-Strain Curve for Sample ' + sample_name + " with 0.2% Yield")

    # plot yield line
    plt.plot(strain, offset_line, label="0.2% Offset Yield")

    # indicate point where yield intersects
    plt.plot(strain[intercept_index], stress[intercept_index], marker='v', label="Yield Strength")

    # since this will go on forever, constrain the axis
    plt.xlim([-.001, max(strain)])
    plt.ylim([0, 1.1 * max(stress)])
    plt.legend()
    plt.show()

    print("Done!")
