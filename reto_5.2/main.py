from Shape import (point, line, shape, rectangle, square, triangle,
            isosceles, equilateral, scalene, trirectangle)

def main():
    print("Bienvenido a mi programa de geometría")

    # Probar la clase Rectangle
    v = point.Point(4, 3)

    rect = rectangle.Rectangle(v, 4, 6)
    print(rect)

    # Probar la clase Square
    sqr = square.Square(v, 4)
    print(sqr)

    # Probar la clase Isosceles
    v1 = point.Point(0, 0)
    v2 = point.Point(4, 0)
    v3 = point.Point(2, 4)
    isos = isosceles.Isosceles(v1, v2, v3)
    print(isos)

    # Probar la clase Equilateral
    v1 = point.Point(0, 0)
    v2 = point.Point(4, 0)
    v3 = point.Point(2, 2 * shape.math.sqrt(3))
    equiltl = equilateral.Equilateral(v1, v2, v3)
    print(equiltl)

    # Probar la clase Scalene
    v1 = point.Point(0, 0)
    v2 = point.Point(4, 0)
    v3 = point.Point(0, 3)
    scalen = scalene.Scalene(v1, v2, v3)
    print(scalen)

    # Probar la clase Trirectangle
    v1 = point.Point(0, 0)
    v2 = point.Point(4, 3)
    tri_rect = trirectangle.Trirectangle(v1, v2)
    print(tri_rect)


if __name__ == "__main__":
    main()
    