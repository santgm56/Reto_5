from Shape.shape import (Point, Rectangle, Square, Isosceles,
Equilateral, Scalene, Trirectangle, math)

def main():
    print("Bienvenido a mi programa de geometría")

    # Probar la clase Rectangle
    v = Point(4, 3)

    rect = Rectangle(v, 4, 6)
    print(rect)

    # Probar la clase Square
    square = Square(v, 4)
    print(square)

    # Probar la clase Isosceles
    v1 = Point(0, 0)
    v2 = Point(4, 0)
    v3 = Point(2, 4)
    isosceles = Isosceles(v1, v2, v3)
    print(isosceles)

    # Probar la clase Equilateral
    v1 = Point(0, 0)
    v2 = Point(4, 0)
    v3 = Point(2, 2 * math.sqrt(3))
    equilateral = Equilateral(v1, v2, v3)
    print(equilateral)

    # Probar la clase Scalene
    v1 = Point(0, 0)
    v2 = Point(4, 0)
    v3 = Point(0, 3)
    scalene = Scalene(v1, v2, v3)
    print(scalene)

    # Probar la clase Trirectangle
    v1 = Point(0, 0)
    v2 = Point(4, 3)
    tri_rect = Trirectangle(v1, v2)
    print(tri_rect)


if __name__ == "__main__":
    main()
    