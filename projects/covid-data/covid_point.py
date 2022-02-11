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
        :param _cases: Number of new cases recorded
        :param _death: Number of new deaths recorded
        """
        self.date = _date
        self.county = _county
        self.state = _state
        self.fips = _fips
        self.cases = _cases
        self.death = _date


