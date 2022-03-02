import pickle

def load_with_pickle(fileName):
    """
    Simple method to load an object from a binary pickle file
    :param fileName: Path where object was saved
    :return: Object that was saved in file
    """
    file = open(fileName, "rb")
    obj = pickle.load(file)
    file.close()
    return obj


class CovidRecord:
    """
    A simple class to hold record data from NYT database
    """

    def __init__(self, _date='', _county='', _state='', _fips=0, _cases=0, _death=0):
        """
        Default constructor for transforming each line of the file into data point

        :param _date: Date covid case was recorded
        :param _county: County in which data was recorded
        :param _state: State in which data was recorded
        :param _fips: Federal Information Processing Standards code
        :param _cases: Number of total cases recorded
        :param _death: Number of total deaths recorded
        """
        self.date = _date
        self.county = _county
        self.state = _state

        if _fips =='':
            self.fips=0
        else:
            self.fips = int(_fips)
        self.cases = int(_cases)

        if _death == '':
            self.death = 0
        else:
            self.death = int(_death)


# all student code goes in the lines below here
if __name__ == "__main__":
    # load covid data as list of CovidRecord objects
    data = load_with_pickle('covid_data.pickle')

    # each element in data is a CovidRecord object. Each of which contains
    # date, county, state, fips, cases, and deaths

    # for example, we can print out the data for the first point in the US counties file
    point = data[0]

    print("Data: ", point.date, " County: ", point.county, " State: ", point.state,
          " FIPS: ", point.fips, " Cases: ", point.cases, " Deaths: ", point.death)

    # write code to address the following question:
    # When was the first positive COVID case in Rockingham County and Harrisonburg?

    # write code to address the following question:
    # What day was the greatest number of new daily cases recorded in Harrisonburg and Rockingham County?

    # write code to address the following question:
    # In terms of absolute number of cases, when was the worst seven day period in the city/county for new COVID cases?

    # write code to address the following question:
    # In terms of absolute number of cases, when was the rise in cases the fastest over a rolling week window?
    # Over what period was the rise in cases the greatest
