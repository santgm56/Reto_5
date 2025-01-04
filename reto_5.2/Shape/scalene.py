from Shape.triangle import Triangle, Point

class Scalene(Triangle):
    """Clase para el triángulo escaleno."""
    def __init__(self, v1: Point, v2: Point, v3: Point):
        super().__init__(v1, v2, v3)

    def is_scalene(self):
        """Determina si el triángulo es escaleno."""
        edges = [edge.compute_length() for edge in self.edges]
        return len(set(edges)) == 3 
    
    """Sobrescribe el cálculo de perímetro para evitar cálculos si 
        no es escaleno."""
    def inner_angles(self):
        if self.is_scalene():
            return super().inner_angles()
        else:
            # Evita realizar cálculos para un triángulo que no es isósceles
            return [0, 0, 0]

    def compute_perimeter(self):
        if self.is_scalene():
            return super().compute_perimeter()
        else:
            #Evita realizar cálculos para un triángulo que no es isósceles
            return 0
    
    def compute_area(self):
        if self.is_scalene():
            return super().compute_area()
        else:
            # Evita realizar cálculos para un triángulo que no es isósceles
            return 0  

    def __str__(self):
        base_str = super().__str__() 
        # Verifica si es isósceles y ajusta la cadena de salida
        if self.is_scalene():
            base_str = base_str.replace("Este triángulo tiene:", 
                                        "Este triángulo escaleno tiene:")
            return f"{base_str} - Es un triángulo escaleno."
        else:
            return f"{base_str} - No es un triángulo escaleno."