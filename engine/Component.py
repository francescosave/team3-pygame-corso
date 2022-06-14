class Component:

  def __init__(self, actor=None):
    self.owner = actor
    self.name = ""

  def load(self):
    pass
  
  def update(self):
    pass

  def render(self, surface):
    pass

  def setOwner(self, actor):
    self.owner = actor