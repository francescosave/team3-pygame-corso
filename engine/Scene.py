from pygame import rect

class Scene:

  def __init__(self):
    self.actors =  []
    self.windowRect = rect.Rect(0,0,0,0)
    
  def load(self):
    for a in self.actors:
      a.load()

  def update(self):
    for a in self.actors:
      a.update()

  def render(self, surface):
    for a in self.actors:
      a.render(surface)
  