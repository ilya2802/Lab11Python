from models.Fortifications import Fortifications

class Escarpment(Fortifications):

    def __init__(self, lenght, depth, time_to_build, number_of_cliffs):
        super().__init__(lenght, depth, time_to_build)
        self.number_of_cliffs = number_of_cliffs

    def __str__(self):
        return str(self.__dict__)
