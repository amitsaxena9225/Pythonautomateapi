class Triangle:

    def __init__(self, height, width):

        self.height = height

        self.width = width

    def area(self):

        return (self.height * self.width)/2


tri = Triangle(10, 5)

print(tri.area())

