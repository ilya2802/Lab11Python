from models.Fortifications import Fortifications

class AntitankNadovb(Fortifications):

    def __init__(self, lenght, depth, time_to_build, kind_of_material):
        super().__init__(lenght, depth, time_to_build)
        self.kind_of_material = kind_of_material

    def __str__(self):
        return str(self.__dict__)
