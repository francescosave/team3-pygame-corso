class Actor:

  def __init__(self):
    self.components = []
    self.x = 0
    self.y = 0  
    self.name = ""

  def load(self):
    for a in self.components:
      a.load()
  
  def update(self):
    for a in self.components:
      a.update()

  def render(self, surface):
    for a in self.components:
      a.render(surface)

  def addComponent(self, component):
    self.components.append(component)
    component.setOwner(self)

  def getDisctionary(self):
    list_components = []
    for item in self.components:
      list_components.append(item.getDisctionary())

    dictionary = {"name": self.name,"x": self.x, "y": self.y, "components": list_components}
    return dictionary
    