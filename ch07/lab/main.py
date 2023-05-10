from Rectangle import Rectangle
from Surface import Surface

def main():
    '''
    ensures the Surface and Rectangle classes work
    and that the recetangle class imports properly to surface.
    '''
    # Test the Rectangle class
    r = Rectangle(10, 10, 10, 10)
    assert((r.x, r.y, r.height, r.width) == (10,10,10,10))

    r = Rectangle(-1, 1, 1, 1)
    assert((r.x, r.y, r.height, r.width) == (1,1,1,1))

    r = Rectangle(1, -5, 1, 1)
    assert((r.x, r.y, r.height, r.width) == (1,5,1,1))

    r = Rectangle(1, 1, -10, 1)
    assert((r.x, r.y, r.height, r.width) == (1,1,10,1))

    r = Rectangle(1, 1, 1, -1000)
    assert((r.x, r.y, r.height, r.width) == (1,1,1,1000))

    # Test the Surface class
    s = Surface("myimage.png", 10, 10, 10, 10)
    assert((s.rect.x, s.rect.y, s.rect.height, s.rect.width) == (10,10,10,10))

    srect = s.getRect()
    assert((srect.x,  srect.y, srect.height,  srect.width) == (10,10,10,10))

    assert s.image

    print("Test Complete!")

if __name__ == '__main__':
    main()
