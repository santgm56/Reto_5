from Shape.shape import Shape, Line, Point, math

class Rectangle(Shape):
    """
    Representa un rectángulo en un espacio bidimensional. 
    El rectángulo puede ser definido de tres maneras:
    1. Dando la esquina inferior izquierda y el ancho y alto.
    2. Dando el centro y el ancho y alto.
    3. Dando dos esquinas opuestas.
    """

    # Atributos de clase
    def __init__(self, *args):
        """
        Se inicializa el rectángulo con una de las siguientes configuraciones:
        - (bottom_left, width, height)
        - (center, width, height)
        - (bottom_left, top_right)
        """
        # Método 1: Esquina inferior izquierda + ancho y alto
        if len(args) == 3 and isinstance(args[0], Point):  
            bottom_left, width, height = args
            self.bottom_left = bottom_left
            self.width = width
            self.height = height
            self.center = Point(
                bottom_left.x + width / 2,
                bottom_left.y + height / 2,
            )
        # Método 2: Centro + ancho y alto
        elif len(args) == 3 and isinstance(args[0], Point) and isinstance(args[1], int):  
            center, width, height = args
            self.center = center
            self.width = width
            self.height = height
            self.bottom_left = Point(
                center.x - width / 2,
                center.y - height / 2,
            )
        elif len(args) == 2:  # Método 3: Dos esquinas opuestas
            bottom_left, top_right = args
            self.bottom_left = bottom_left
            self.width = top_right.x - bottom_left.x
            self.height = top_right.y - bottom_left.y
            self.center = Point(
                bottom_left.x + self.width / 2,
                bottom_left.y + self.height / 2,
            )
        else:
            raise ValueError("""Número de argumentos inválido para 
                            inicializar un rectángulo.""")

    def vertices(self):
        """Calcula los vértices del rectángulo."""
        return [
            self.bottom_left,
            Point(self.bottom_left.x + self.width, self.bottom_left.y),
            Point(self.bottom_left.x + self.width, self.bottom_left.y + self.height),
            Point(self.bottom_left.x, self.bottom_left.y + self.height),
        ]
    
    def edges(self):
        """Devuelve las líneas que forman los lados del rectángulo."""
        v = self.vertices()
        return [
            Line(v[0], v[1]),
            Line(v[1], v[2]),
            Line(v[2], v[3]),
            Line(v[3], v[0]),
        ]
    
    def inner_angles(self) -> list[float]:
        """Imprime los ángulos internos del rectángulo."""
        return self.compute_inner_angles()
    
    def is_regular(self) -> bool:
        """Determina si el rectángulo es regular."""
        return self.width == self.height
    
    def compute_perimeter(self) -> float:
        """Calcula el perímetro del rectángulo."""
        return 2 * (self.width + self.height)
    
    def compute_area(self) -> float:
        """Calcula el área del rectángulo."""
        return self.width * self.height

    def compute_inner_angles(self):
        """Devuelve los ángulos internos en radianes."""
        # Cada ángulo es 90 grados = π/2 radianes
        return [round(math.pi / 2, 4)] * 4 
    
    def __str__(self):
        # Generar información con cálculos
        vertices_str = ", ".join([f"({v.x}, {v.y})" for v in self.vertices()])
        edges_str = ", ".join([f"({e.start.x}, {e.start.y}) -> ({e.end.x}, {e.end.y})" for e in self.edges()])
        
        return (
            f"Este Rectángulo tiene las siguientes especificaciones:\n"
            f"- Esquina inferior izquierda: ({self.bottom_left.x}, {self.bottom_left.y})\n"
            f"- Dimensiones: Ancho = {self.width}, Alto = {self.height}\n"
            f"- Área: {self.compute_area()}\n"
            f"- Perímetro: {self.compute_perimeter()}\n"
            f"- Ángulos internos: {self.inner_angles()}\n"
            f"- Es regular: {'Sí' if self.is_regular() else 'No'}\n"
            f"- Vértices: {vertices_str}\n"
            f"- Lados (aristas): {edges_str}"
        )