class Point:
    """
    Entidad geometrica abstracta que representa una ubicación en un espacio.
    """

    # Este método inicializa los valores de x y y del punto a los valores 
    # pasados como parámetros.
    def __init__(self, x: float=0, y: float=0):
        self.__x = x
        self.__y = y

    # Setters and Getters de los atributos de Point
    
    """
    @property define un método que se comporta como un atributo de solo 
    lectura. Le agrega la funcionalidad de un getter.
    """
    @property
    def x(self):
        return self.__x
    
    """
    @x.setter define un método que se comporta como un atributo de solo 
    lectura escritura. Le agrega la funcionalidad de un setter.
    """
    @x.setter
    def x(self, value_x: float):
        self.__x = value_x

    @property
    def y(self):
        return self.__y
    
    @y.setter
    def y(self, value__y: float):
        self.__y = value__y
        
    # Este método calcula la distancia entre dos puntos    
    def compute_distance(self, point: "Point")-> float:
        distance = ((self.x - point.x) ** 2 + (self.y - point.y) ** 2 ) ** (0.5)
        return distance
    
    def __str__(self):
        return f"({self.x}, {self.y})"