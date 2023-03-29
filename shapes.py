class Square:
    """A Square that can be drawn into a canvas"""
    def __init__(self, x, y, side, color):
        self.x = x
        self.y = y
        self.side = side
        self.color = color

    def draw(self, canvas):
        """Draws itself into the given canvas"""

        #Change a slice of the array into a new color
        canvas.data[self.x:self.x+self.side, self.y:self.y+self.side] = self.color



class Rectangle:
    """A Rectangle that can be drawn into a canvas"""
    def __init__(self, x, y, height, width, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self, canvas):
        """Draws itself into the given canvas"""
        
        #Change a slice of the array into a new color
        canvas.data[self.x:self.x+self.width, self.y:self.y+self.height] = self.color