import math
import unittest

def classifyTriangle(a, b, c):
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        return 'not a triangle'
    elif a == b and b == c:
        return 'equilatteral'
    elif (a == b or b == c or a == c):
        return 'isosceles'
    elif not (a == b or b == c or a == c):
        return 'scalene'
    elif a**2 + b**2 == c**2:
        return 'right' 
    else:
        return ''

def runClassifyTriangle(a, b, c):
    print('classifyTriangle(', a, ',', b, ',', c, ') = ',classifyTriangle(a,b,c),sep="")

class TestTriangles(unittest.TestCase):
    def testScalene(self):
        self.assertEqual(classifyTriangle(4, 3, 2), 'scalene', '4,1,2 should be scalene')
        self.assertNotEqual(classifyTriangle(4, 1, 2), 'scalene', '4,1,2 should be scalene')

    def testIsosceles(self):   
        self.assertEqual(classifyTriangle(4, 3, 3), 'isosceles', '4, 3, 3 should be isosceles')
        self.assertNotEqual(classifyTriangle(4, 4, 4), 'isosceles', '4,4,4 should not be isosceles')

    def testEquilateral(self):   
        self.assertEqual(classifyTriangle(4, 4, 4), 'equilateral', '4,4,4 should be equilateral')
        self.assertNotEqual(classifyTriangle(4, 2, 4), 'equilateral', '4,2,4 should not be equilateral')

    def testInput(self):
        self.assertEqual(classifyTriangle(1, 2, 3), 'not a triangle', '1,2,3 should not be a triangle')

if __name__ == "__main__":
    runClassifyTriangle(1, 2, 3)
    runClassifyTriangle(1, 1, 1)
    runClassifyTriangle(2, 2, 3)

    unittest.main(exit=True)
