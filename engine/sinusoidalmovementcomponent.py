from .component import *
import math


class SinusoidalMovementComponent(Component):
    
    # Owner could be empty at first
    def __init__(self, actor = None):
        super().__init__(actor)
        self.amp = 100
        self.vx = 0.05
        self.angle = 0
        

    # I could implement some debugging rendering here
    def render(self, surface):
        pass

    # There will be timing involved
    def update(self):
        self.angle += 0.005
        self.owner.x += self.vx 
        self.owner.y = math.sin(self.angle)*self.amp + 700

        #bounce
        if self.owner.x < 0 or self.owner.x > 600:
            self.vx = -self.vx
        


