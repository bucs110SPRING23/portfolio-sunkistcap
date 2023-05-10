#import modules
from Rectangle import Rectangle

class Surface:
    
    def __init__(self,filename,x,y,h,w):
        """
        Initializes a Surface object with an  allocated image and a rectangle.

        Parameters:
            filename:str The name of the image file.
            x:int The x coordinate of the top-left corner of the rectangle.
            y:int The y coordinate of the top-left corner of the rectangle.
            h:int The height of the rectangle.
            w:int The width of the rectangle.
        """
        self.rect=Rectangle(x,y,h,w)
        self.image=str(filename)
    
    def getRect(self):
        '''
        returns the rectangle attributes from the rectangle class

        return:
            :Rectangle = rectangle created in the rectangle class
        '''
        return self.rect
    