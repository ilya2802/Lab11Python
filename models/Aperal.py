from models.Fortifications import Fortifications

class Aperal(Fortifications):

    def __init__(self, lenght, depth, time_to_build, angle_of_inclination):
        super().__init__(lenght, depth, time_to_build)
        self.angle_of_inclination = angle_of_inclination

    def __str__(self):
        return str(self.__dict__)
