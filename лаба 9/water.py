"""
Модуль, що працює з водою.

Надає функції для обробки води.
"""

def boil_water():
    """Кип'ятить воду."""
    print("Boiling water...")

class water:
    def __init__(self, name: str = "Unknown", type: str = "Unknown",
                 area: float = 0.0, depth: float = 0.0, location: str = "Unknown",
                 water_volume: float = 0.0, is_fresh: bool = False, origin: str = "Unknown"):
        self.name = name
        self.type = type
        self.area = area
        self.depth = depth
        self.location = location
        self.water_volume = water_volume
        self.is_fresh = is_fresh
        self.origin = origin


    def printAllAtributes(self):    
        print(f"All attributes of {self.name}:")
        print(f"  Name: {self.name}")
        print(f"  Type: {self.type}")
        print(f"  Area: {self.area}")
        print(f"  Depth: {self.depth}")
        print(f"  Location: {self.location}")
        print(f"  Water volume: {self.water_volume}")
        print(f"  Fresh: {self.is_fresh}")
        print(f"  Origin: {self.origin}")
    
    def getVolume(self):
        return self.water_volume
    
    def setVolume(self , newVolume):
        self.water_volume = newVolume