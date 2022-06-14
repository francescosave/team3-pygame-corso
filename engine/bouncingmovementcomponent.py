from .component import *

class BouncingMovementComponent(Component):
  def __init__(self, boundingRect, actor=None):
    super().__init__(actor)
    self.vx = 0.05
    self.vy = 0.05
    self.boundingRect = boundingRect
  
  def render(self, surface):
    pass
  
  def update(self):
    self.owner.x += self.vx
    self.owner.y += self.vy

    # bounce on the x axis
    if self.owner.x < 0 or self.owner.x > self.boundingRect.width:
        self.vx = -self.vx
    
    # bounce on the y axis
    if self.owner.y < 0 or self.owner.y > self.boundingRect.height:
        self.vy = -self.vy