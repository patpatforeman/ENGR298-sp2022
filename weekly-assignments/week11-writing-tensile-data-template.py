import numpy as np
import os
import math
import sys


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
    cross_sectional_area = math.pi * (sample_diameter / 2) ** 2

    # calculate stress (MPa) from load (kN) and cross-sectional area
    stress = force / cross_sectional_area * 1000

    return stress


def calculate_max_strength_strain(strain, stress):
    """
    Calculate the Ultimate Tensile Stress and Fracture Strain
    :param strain: An array of Strain data (MPa)
    :param stress: An array of Stress data
    :return:
    Ultimate Tensile Stress: the maximum stress experienced
    Fracture Strain: the maximum strain experienced before fracture
    """

    ultimate_tensile_stress = max(stress)

    fracture_strain = max(strain)

    return ultimate_tensile_stress, fracture_strain


def calculate_elastic_modulus(strain, stress):
    """
    Given a set of stress strain data, use the Secant Modulus at 40% method to determine
    the elastic modulus
    :param strain: An array of Strain data (MPa)
    :param stress: An array of Stress data
    :return:
    linear_index: the index within the strain/stress data that is the end of the linear region
    slope: the slope for the linear region of the strain/stress data
    intercept: y-intercept for linear region best fit of strain/stress data
    """

    # Step 3a: find the point that is 40% of peak strain
    # use from 0 to that value to create a linear plot
    secant_strain = max(stress) * 0.40

    # Step 3b: find the index closes to that
    # take the diff of the whole array and argmin
    diffs = np.abs(stress - secant_strain)
    linear_index = np.argmin(diffs)

    # Step 3c: down select to linear region for stress and strain
    linear_stress = stress[0:linear_index]
    linear_strain = strain[0:linear_index]

    # Step 3d: find least squares fit to a line in the linear region
    # use 1-degree polynominal fit (line)
    slope, intercept = np.polyfit(linear_strain, linear_stress, 1)

    return linear_index, slope, intercept

def calculate_yield_strength(strain, stress, modulus, offset=0.002):
    """
    Determine the yield strength via 0.2% offset method
    :param strain: An array of Strain data (mm/mm)
    :param stress: An array of Stress data (MPa)
    :param modulus: The elastic modulus of the material
    :param offset: Desired offset. Default is 0.002 (0.2%)
    :return: Y-intercept of line that originates at (0,.002) with modulus slope
    """

    # next to find point that intersects y=m(x-0.002) + 0
    # calculate the offset line
    offset_line = modulus * (strain - offset)

    # measure distance from all points on graph to this line
    distance = abs(stress - offset_line)
    intercept_index = np.argmin(distance)

    return stress[intercept_index]


class MaterialSample:
    """
    A simple class to hold results from materials tensile analysis
    """

    def __init__(self):
        self.name = ""
        self.material_type = ""
        self.tensile_strength = -1
        self.fracture_strain = -1
        self.elastic_modulus = -1
        self.yield_strength = -1


def generate_csv_file(filename, results):
    """
    A function to take a list of material strength results and print to a CSV file
    :param filename: File that should be written to
    :param results: Material strength results as list of Material Sample objects
    :return: True if data was written out to the file successfully, false otherwise
    """

    # Step 1: create a variable to hold the file name

    # uncomment this line
    #output_file_name = ### your code here ###

    # Step 2: use open() to open the file in write mode. Set the return of open()
    # to a variable name that will be your file handle

    # uncomment the line below
    #file = ### your code here ###

    # Step 3: write out the header for the CSV file. This string is provided for you so
    # your data can be loaded and checked. Use write().
    file_header = "Sample_Name,Material_Type,Tensile_Strength,Fracture_Strain,Elastic_Modulus,Yield_Strength\n"

    # write header string out to file
    #file.### your code here ###

    # Step 4: Iterate through the list of results. Each sample will contain the data for an individual test
    for r in results:

        # Each object in the results list is of class SampleMaterial. This is just a dummy class to hold variables
        # in a single object. For your ease they have been broken out into individual variable names
        name = r.name
        material_type = r.material_type
        tensile_strength = r.tensile_strength
        fracture_strain = r.fracture_strain
        modulus = r.elastic_modulus
        yield_strength = r.yield_strength

        # Step 5: Stitch together a string, then write out the string via write().
        # Many variables above must be converted to a string via (). Commas also must be manually
        # stitched between each variable in the output. Do not round the data
        # Make sure an endline character '\n' is always at the end of your string!

        # uncomment the line below
        #string_to_write = ### your code here ###

        # Finally, given that long string, write it to a file

        ### your code here ###

    # close the file once all writing is complete
    file.close()

    # since we got here, it must have worked.
    return True

if __name__ == "__main__":

    # get path to data/ folder
    path_to_tensile_folder = "../data/tensile/"

    # list to hold all sample results
    results = []

    # each folder in data/ is a different material
    materials = list()
    for root, dirs, files in os.walk(path_to_tensile_folder):
        materials.extend(dirs)
        break

    # now walk through each material and file
    for material in materials:
        print("Parsing material: ", material)

        # walk through folder
        path_to_material_folder = path_to_tensile_folder + material + "/"
        for root, dirs, files in os.walk(path_to_material_folder):

            # parse each file that was found
            for file_name in files:
                print("\tLoad sample: ", file_name)

                # create path to sample file
                path_to_sample = path_to_material_folder + file_name

                # Parse the file ane return based values
                # sample diameter (mm), time (s), displacement (mm), force (kN), and strain (%)
                sample_diameter, time, displacement, force, strain = parse_tensile_file(path_to_sample)

                # Given the forces and sample diameter, calculate the strain
                stress = calculate_stress(force, sample_diameter)

                if stress is None:
                    print("Error! No stress returned. Did you fill in the calculate_stress() method?")
                    sys.exit(-1)

                # calculate easy variables
                ultimate_tensile_strength, fracture_strain = calculate_max_strength_strain(strain, stress)

                if ultimate_tensile_strength == -1 or fracture_strain == -1:
                    print("Error! Tensile Strength or Fracture Strain returned as -1. Did you complete the calculate_max_strength() method?")
                    sys.exit(-1)

                # Use the Secant Modulus at 40% of Peak Stress
                # to determine elastic modulus
                linear_index, slope, intercept = calculate_elastic_modulus(strain, stress)

                elastic_modulus = slope / 1000

                # Calculate Yield Strength
                yield_strength = calculate_yield_strength(strain, stress, slope)

                # create a new material sample
                sample = MaterialSample()
                sample.name = file_name.split(".")[0]
                sample.material_type = material
                sample.tensile_strength = ultimate_tensile_strength
                sample.fracture_strain = fracture_strain
                sample.elastic_modulus = elastic_modulus
                sample.yield_strength = yield_strength

                # place in list
                results.append(sample)

    # manually print out the results to see what you have
    for r in results:
        print("Sample Name: ", r.name)
        print("\tMaterial Type: ", r.material_type)
        print("\tTensile Strength: ", r.tensile_strength)
        print("\tFracture Strain: ", r.fracture_strain)
        print("\tElastic Modulus: ", r.elastic_modulus)
        print("\tYield Strength: ", r.yield_strength)

    generate_csv_file('tensile_data.csv',results)

    print("Done!")


