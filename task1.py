class Circle:
    def __init__(self, radius):
        self.__radius = radius
    
    def get_radius(self):
        return self.__radius
    
    def set_radius(self, radius):
        self.__radius = radius
    
    def area(self):
        return 3.14 * self.__radius ** 2
    
    def circumference(self):
        return 2 * 3.14 * self