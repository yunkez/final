import pickle


def read_file(filename):
    try:
        with open('../data/' + filename, 'rb') as f:
            file = pickle.load(f)
        return file
    except FileNotFoundError:
        return None
