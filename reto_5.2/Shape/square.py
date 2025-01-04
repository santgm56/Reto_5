from Shape.rectangle import Rectangle, Point

class Square(Rectangle):
    """
    Clase que representa un cuadrado, un caso especial de un rectángulo donde 
    el ancho y la altura son iguales.
    """

    def __init__(self, bottom_left: Point, side_lenght: float):
        """
        Se inicializa el cuadrado con la esquina inferior izquierda 
        y el lado
        """
        super().__init__(bottom_left, side_lenght, side_lenght)
    
    def compute_area(self):
        return self.width ** 2
    
    def __str__(self):
        """Se reutiliza la lógica del dunder method __str__ de Rectangle 
        pero ajustar el encabezado"""
        rect_str = super().__str__()
        return rect_str.replace("Rectángulo", "Cuadrado")