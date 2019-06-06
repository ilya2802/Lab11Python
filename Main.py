from models.Fortifications import Fortifications
from models.AntitankNadovb import AntitankNadovb
from models.Aperal import Aperal
from models.Blindage import Blindage
from models.Escarpment import Escarpment
from models.Trench import Trench
from Enums.kindOfCovering import KindOfCovering
from Enums.KindOfMaterial import KindOfMaterial
from manager.FortificationManager import FortificationManager

def main():
    antitank_nadovb = AntitankNadovb(46,37,31,KindOfMaterial.CONCRETE)
    aperal = Aperal(37, 87, 16, 3)
    escarpment = Escarpment(29, 41, 19, 4)
    blindage = Blindage(47, 23, 55, KindOfCovering.FERROCONCRETE, 3, 47)
    trench = Trench(45, 65, 38, 21)

    fortification_manager = FortificationManager([antitank_nadovb, aperal, escarpment, blindage, trench])

    a = fortification_manager.find_items_by_time(31)
    b = fortification_manager.find_items_by__length(37)
    c = fortification_manager.sort_by_depth(True)

    print(a)
    print(b)
    print(c)


if __name__ == '__main__':
    main()
