from Shape.shape import Shape, Line, Point, math

class Triangle(Shape):
    """
    Representa un triángulo en un espacio bidimensional. 
    """
    def __init__(self, v1: Point, v2: Point, v3: Point):
        self.__v1 = v1
        self.__v2 = v2
        self.__v3 = v3

        if not self.is_valid_triangle():
            print("Los puntos no forman un triángulo válido")
        
    def is_valid_triangle(self):
        # Calcular las longitudes de los lados
        d1 = Line(self.__v1, self.__v2).compute_length()
        d2 = Line(self.__v2, self.__v3).compute_length()
        d3 = Line(self.__v3, self.__v1).compute_length()

        # Comprobación de la regla básica para formar un triángulo
        return (d1 + d2 > d3) and (d2 + d3 > d1) and (d1 + d3 > d2)

    @property
    def v1(self) -> Point:
        return self.__v1
    
    @v1.setter
    def v1(self, point: Point):
        self.__v1 = point

    @property
    def v2(self) -> Point:
        return self.__v2
    
    @v2.setter
    def v2(self, point: Point):
        self.__v2= point

    @property
    def v3(self) -> Point:
        return self.__v3
    
    @v3.setter
    def v3(self, point: Point):
        self.__v3 = point

    def vertices(self):
        """Calcula los vértices del triángulo."""
        return [self.__v1, self.__v2, self.__v3]

    @property
    def edges(self) -> list[Line]:
        """Calcula los lados del rectángulo."""
        v = self.vertices()
        return [
            Line(v[0], v[1]),
            Line(v[1], v[2]),
            Line(v[2], v[0]),
        ]
    
    def inner_angles(self):
        """Imprime los ángulos internos del triángulo."""
        return self.compute_inner_angles()

    def is_regular(self):
        """Determina si el triángulo es regular."""
        return all([line.compute_length() == self.edges[0].compute_length() for line in self.edges])
    
    def compute_perimeter(self):
        """Calcula el perímetro del triángulo."""
        return sum([line.compute_length() for line in self.edges])

    def compute_area(self):
        """Calcula el área del triángulo."""
        # Herón's formula
        a = self.edges[0].compute_length()
        b = self.edges[1].compute_length()
        c = self.edges[2].compute_length()
        s = (a + b + c) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))
    
    def compute_inner_angles(self):
        """
        Calcula los ángulos internos utilizando la ley del coseno.
        Devuelve los ángulos en radianes.
        """
        a = self.edges[0].compute_length()
        b = self.edges[1].compute_length()
        c = self.edges[2].compute_length()

        # Ley del coseno para hallar los ángulos
        angle_A = math.acos((b**2 + c**2 - a**2) / (2 * b * c))
        angle_B = math.acos((a**2 + c**2 - b**2) / (2 * a * c))
        angle_C = math.acos((a**2 + b**2 - c**2) / (2 * a * b))

        return [round(angle, 6) for angle in [angle_A, angle_B, angle_C]]
    
    def __str__(self):
        vertices_str = ", ".join([f"({v.x}, {v.y})" for v in self.vertices()])
        edges_str = ", ".join([f"({e.start.x}, {e.start.y}) -> ({e.end.x}, {e.end.y})" for e in self.edges])

        return (
            f"Este triángulo tiene las siguientes especificaciones:\n"
            f"- Vértices: {vertices_str}\n"
            f"- Lados (aristas): {edges_str}\n"
            f"- Área: {self.compute_area()}\n"
            f"- Perímetro: {self.compute_perimeter()}\n"
            f"- Ángulos internos: {self.inner_angles()}\n"
            f"- Es regular: {'Sí' if self.is_regular() else 'No'}"
    )
