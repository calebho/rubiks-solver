import unittest

from cube import Cube

class TestCube(unittest.TestCase):
    def setUp(self):
        self.c = Cube()

    def test_rotate(self):
        faces = ['front','back','right','left','up','down']

        for face in faces:
            self.c.rotate(face, 'r').rotate(face, 'l')
            self.assertTrue(self.c.is_solved())

            for dir_ in ['r','l']:
                for i in range(4):
                    self.c.rotate(face, dir_)
                self.assertTrue(self.c.is_solved())

if __name__ == "__main__":
    unittest.main()
