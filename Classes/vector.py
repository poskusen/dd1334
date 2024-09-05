class Vector:

    def __init__(self, firstpos, secondpos, nextvector=None):
        self.nextvector = nextvector
        self.firstpos = firstpos
        self.secondpos = secondpos

