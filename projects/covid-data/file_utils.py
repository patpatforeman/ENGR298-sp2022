import pickle


def save_with_pickle(fileName, obj):
    """
    Simple method to save an object as a binary pickle
    :param fileName: Path where object will be saved
    :param obj: Objects to be saved
    :return: None
    """
    file = open(fileName, "wb")
    pickle.dump(obj, file)
    file.close()


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
