from models.Fortifications import Fortifications

class Trench(Fortifications):

    def __init__(self, lenght, depth, time_to_build, width):
        super().__init__(lenght, depth, time_to_build)
        self.width = width

    def __str__(self):
        return str(self.__dict__)
