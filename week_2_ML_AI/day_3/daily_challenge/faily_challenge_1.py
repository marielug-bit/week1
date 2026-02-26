import math
class Circle:

    def __init__(self,radius):
        self.radius = radius

    @property
    def diameter(self):
        return self.radius*2
    
    def area(self):
        return math.pi * self.radius ** 2
    
    def __str__(self):
        return f'Circle(radius={self.radius})'
    
    def __add__(self,other:Circle):
        new_circle = Circle(self.radius + other.radius)
        return new_circle
    
    def __gt__(self,other:Circle):
        return self.radius > other.radius
    
    def __eq__(self,other:Circle):
        return self.radius == other.radius
    
    def __lt__(self,other):
        return self.radius < other.radius
    
circles = [Circle(8), Circle(3), Circle(12), Circle(1), Circle(5)]
for c in sorted(circles):
    print(f"  {c} — area: {c.area():.2f}")



