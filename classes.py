class Coordinate():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calculate_distance(self, other):
        x_distance = (self.x - other.x) **2
        y_distance = (self.y - other.y) **2

        return (x_distance + y_distance) ** 0.5
    
    def __str__(self):
        return "<" + str(self.x) + ", " + str(self.y) + ">"
    

origin = Coordinate(0, 0)
new = Coordinate(2, 3)
print(new)
print(origin.calculate_distance(new))
