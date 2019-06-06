class Fortifications:

    def __init__(self, lenght, depth, time_to_build):
        self.lenght = lenght
        self.depth = depth
        self.time_to_build = time_to_build

    def __str__(self):
        return str(self.__dict__)
