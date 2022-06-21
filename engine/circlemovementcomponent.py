from .component import *
import math


class CircleMovementComponent(Component):
    
    # Owner could be empty at first
    def __init__(self, radius, center_x, center_y, actor = None):
        super().__init__(actor)
        self.radius = radius
        self.center_x = center_x
        self.center_y = center_y
        self.angle = 0

    # I could implement some debugging rendering here
    def render(self, surface):
        pass

    # There will be timing involved
    def update(self):
        
        self.angle += 0.005
        
        self.owner.x = self.radius * math.cos(self.angle) + self.center_x
        self.owner.y = self.radius * math.sin(self.angle) + self.center_y

    def getDisctionary(self):
      dictionary = {"name": self.name,"type" : self.__class__.__name__ , "center_x": self.center_x, "center_y": self.center_y, "radius" : self.radius}
      return dictionary
        

