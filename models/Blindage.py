from models.Fortifications import Fortifications

class Blindage(Fortifications):

    def __init__(self, lenght, depth, time_to_build, kind_of_covering, capacity_of_people, square):
        super().__init__(lenght, depth, time_to_build)
        self.kind_of_covering = kind_of_covering
        self.capacity_of_people = capacity_of_people
        self.square = square

    def __str__(self):
        return str(self.__dict__)
