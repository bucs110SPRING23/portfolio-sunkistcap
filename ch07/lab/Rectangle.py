class Rectangle:
    def __init__(self, x, y, h, w):
        """
        attributes to create a rectangle

        Parameters:
            x:int The x coordinate of the top-left corner of the rectangle.
            y:int The y coordinate of the top-left corner of the rectangle.
            h:int The height of the rectangle.
            w:int The width of the rectangle.
        """
        self.x = abs(x)
        self.y = abs(y)
        self.height = abs(h)
        self.width = abs(w)

    def __str__(self):
        '''
        returns the dimensions of the rectangle that was made

        return:
            = rectangle's current dimensions and position
        '''
        return "(x: "+ str(self.x)+", y: "+ str(self.y)+") width: "+str(self.width)+", height: "+str(self.height)        