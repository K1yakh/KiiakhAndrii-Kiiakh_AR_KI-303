"""
Модуль, що реалізує логіку морської тематики.

Містить функції для роботи з морем.
"""

def sail_boat():
    """Запускає процес плавання човна."""
    print("Sailing the boat...")

from water import *
class Sea(water):
    def __init__(self, salinity: float = 0.0 , number_of_islands: int = 0,
                 climate_zone: str = "Unknow", has_tides: bool = False,
                 adjoining_oceans: str = "Unknown", largest_port: str = "Unknown",
                 name: str = "Unknown", area: float = 0.0, depth: float = 0.0,
                 location: str = "Unknown", water_volume: float = 0.0,
                 origin: str = "Unknown"):
        
        super().__init__(name, "Sea", area, depth, location, water_volume, False, origin)

        self.salinity = salinity
        self.number_of_islands = number_of_islands
        self.climate_zone = climate_zone
        self.has_tides = has_tides
        self.adjoining_oceans = adjoining_oceans
        self.largest_port = largest_port

    def printAllAttributes(self):
        super().printAllAtributes()
        print(f"  Salinity: {self.salinity}‰")
        print(f"  Number of Islands: {self.number_of_islands}")
        print(f"  Climate Zone: {self.climate_zone}")
        print(f"  Has Tides: {self.has_tides}")
        print(f"  Adjoining Oceans: {self.adjoining_oceans}")
        print(f"  Largest Port: {self.largest_port}")