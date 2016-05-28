"""
Rubiks cube class
"""

import numpy as np

def swap(d, key1, key2):
    """Given a dictionary `d`, swap the values at keys `key1` and `key2`
    """
    d[key1], d[key2] = d[key2], d[key1]

def shift(d, keys, dir_):
    """Given a dictionary `d`, a sequence of keys `keys`, and a direction `dir`
    move the values in `d` corresponding to `keys` one space over in the
    direction `dir`

    i.e.:
    d = {'a':1, 'b':2, 'c':3}
    right_shift(d) -> {'a':3, 'b':1, 'c':2}
    """
    if dir_ == 'r':
        last = d[keys[-1]]
        for i in range(0, len(keys) - 1):
            d[keys[i + 1]] = d[keys[i]]
        d[keys[0]] = last
    else:
        first = d[keys[0]]
        for i in range(len(keys) - 1, 0, -1):
            d[keys[i - 1]] = d[keys[i]]
        d[keys[-1]] = first

class Cube(object):
    def __init__(self):
        self._state = {'front': np.chararray((3,3)),
                      'back': np.chararray((3,3)),
                      'right': np.chararray((3,3)),
                      'left': np.chararray((3,3)),
                      'up': np.chararray((3,3)),
                      'down': np.chararray((3,3))}

        faces = ['front','back','right','left','up','down'] # ensure order of faces
        colors = ['b','g','r','o','y','w'] # each pair are opposite faces
        for face, color in zip(faces, colors):
            self._state[face][:] = color

    def __str__(self):
        """2D representation of cube
        """
        to_ret = '\n'
        # upper face
        for row in range(3):
            to_ret += ' ' * 6
            for col in range(3):
                to_ret += self._state['up'][row, col] + ' '
            to_ret += '\n'

        # left, front, right, back faces
        for row in range(3):
            for face in ['left','front','right','back']:
                for col in range(3):
                    to_ret += self._state[face][row, col] + ' '
            to_ret += '\n'

        # lower face
        for row in range(3):
            to_ret += ' ' * 6
            for col in range(3):
                to_ret += self._state['down'][row, col] + ' '
            to_ret += '\n'

        return to_ret

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, s):
        self._state = s

    def shuffle(self):
        pass

    def is_solved(self):
        for face in self._state:
            vals = self._state[face].flatten()
            for color in vals:
                if color != vals[0]:
                    return False

        return True

    def select(self, face):
        """Selects a face for rotation
        """
        if face == 'front':
            return
        elif face == 'back':
            swap(self._state, 'front', 'back')
            swap(self._state, 'left', 'right')
        elif face == 'right':
            shift(self._state, ['left','front','right','back'], 'l')
        elif face == 'left':
            shift(self._state, ['left','front','right','back'], 'r')
        elif face == 'up':
            shift(self._state, ['down','front','up','back'], 'l')
        elif face == 'back':
            shift(self._state, ['down','front','up','back'], 'r')


    def rotate(self, dir_):
        """Rotates front face in `dir_` direction
        """
        if not self._selected:
            raise RuntimeError("No face selected")

if __name__ == "__main__":
    c = Cube()
    print c
