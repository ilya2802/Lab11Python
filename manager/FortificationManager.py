from models.Fortifications import Fortifications
from models.AntitankNadovb import AntitankNadovb
from models.Aperal import Aperal
from models.Blindage import Blindage
from models.Escarpment import Escarpment
from models.Trench import Trench
from Enums.kindOfCovering import KindOfCovering
from Enums.KindOfMaterial import KindOfMaterial

class FortificationManager:

    def __init__(self, fortifications_list):
        self.fortifications_list = fortifications_list

    def find_items_by_time(self, time):
        return list(filter(lambda fortification:fortification.time_to_build == time, self.fortifications_list))

    def find_items_by__length(self, length):
        return list(filter(lambda fortification:fortification.lenght == length, self.fortifications_list))

    def sort_by_depth(self, reverse):
        return sorted(self.fortifications_list, key=lambda fortification:fortification.depth, reverse=reverse)
