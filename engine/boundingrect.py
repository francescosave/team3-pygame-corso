class BoundingRect:

    def __init__(self,boundingrect):
        self.x = boundingrect.x
        self.y = boundingrect.y
        self.width = boundingrect.width
        self.height = boundingrect.height

    def getDisctionary(self):
        dictionary = {"x": self.x, "y": self.y, "width": self.width, "height": self.height}
        return dictionary