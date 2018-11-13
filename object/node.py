class Node:
    def __init__(self, id=None, key=None):
        self.id = id
        self.key = key

    def __lt__(self, other):
        return self.id < other.id

    def __gt__(self, other):
        return other.__lt__(self)

    def __eq__(self, other):
        return self.id == other.id