def main():

    # * Classes

    class Circle:
        def __init__(self, radius, color):
            self.radius = radius
            self.color = color

        def add_radius(self, r):
            self.radius += r
            return self.radius

    class Rectangle:
        def __init__(self, heigth, width):
            self.heigth = heigth
            self.width = width

    C1 = Circle(10, "red")
    # TODO: obtain the list of data attributes and methods associated
    print(dir(C1))

    # TODO: create an object
    C2 = Circle(color = "blue", radius = 3)
    print(C2.radius)

    L = [5,4,6]
    L.sort()
    print(L)

main()
