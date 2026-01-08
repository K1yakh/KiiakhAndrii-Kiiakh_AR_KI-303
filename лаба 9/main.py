"""
Модуль головного запуску програми.

Цей модуль містить основну логіку роботи.
"""

def start_app():
    """Запускає основну логіку програми."""
    print("App started!")

from water import *
from sea import *

dnipro = water("Tyasmin", "River", 10, 30, "Ukraine", 55.3, False, "unknown")

dnipro.printAllAtributes()

Unknown = water()

Unknown.printAllAtributes()

RedSea = Sea(
    salinity=40.0,  
    number_of_islands=1100,  
    climate_zone="Tropical to subtropical",
    has_tides=True,
    adjoining_oceans="Atlantic Ocean (via the Bab-el-Mandeb Strait)",
    largest_port="Jeddah",
    name="Black Sea",
    area=438000.0,  
    depth=490.0,  
    location="Middle East and Northeast Africa",
    water_volume=233000.0,  
    origin="Rift valley/Tectonic"
)
blueSea = Sea()

RedSea.printAllAttributes()
blueSea.printAllAttributes()


print(f"Blue sea volume = {dnipro.getVolume()}\n")
dnipro.setVolume(55)
print(f"Blue sea volume = {dnipro.getVolume()}\n")