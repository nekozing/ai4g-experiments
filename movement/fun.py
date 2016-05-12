import unittest

class Static(object):
    def __init__(self, position = None, orientation = None):
        # Vector2d
        self.position = position
        # floating point
        self.orientation = orientation
    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__
    def __str__(self):
        return "pos: {}, orientation: {}".format(self.position, self.orientation)
    def __repr__(self):
        return str(self)

class Vector2d(object):
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__
    def __str__(self):
        return "({}, {})".format(self.x, self.y)
    def __repr__(self):
        return str(self)

class TestFun(unittest.TestCase):
    def testVector(self):
        v = Vector2d(0, 0)
        w = Vector2d(0, 0)
        self.assertEqual(v, w)
    def testStaticInit(self):
        s = Static(Vector2d(0,0), 0)
        self.assertEqual(s.position, Vector2d(0, 0))
        self.assertEqual(s.orientation, 0)


if __name__ == "__main__":
    unittest.main()