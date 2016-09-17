"""
Rubiks cube class
"""

import numpy as np

from random import choice
from copy import copy

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

    def shuffle(self, n=50):
        faces = self._state.keys()
        directions = ['r', 'l']
        for i in range(n):
            face = choice(faces)
            direction = choice(directions)
            self.rotate(face, direction)

    def is_solved(self):
        for face in self._state:
            vals = self._state[face].flatten()
            for color in vals:
                if color != vals[0]:
                    return False

        return True

    def rotate(self, face, dir_):
        """Rotates face `face` in `dir_` direction
        """
        if dir_ == 'r': # clockwise
            k = 3
        else:
            k = 1

        self._select(face)
        self._state[face] = np.rot90(self._state[face], k) # rotates counterclockwise
        self._shift_sides(face, dir_)
        self._deselect(face)

        return self

    def _select(self, face):
        """Selects a face for rotation by orienting adjacent faces properly
        """
        if face == 'front':
            pass
        elif face == 'back':
            self._state['up'] = np.rot90(self._state['up'], 2) # rotate 180
            self._state['down'] = np.rot90(self._state['down'], 2)
        elif face == 'right':
            self._state['up'] = np.rot90(self._state['up'], 3) # counterclockwise 90
            self._state['down'] = np.rot90(self._state['down'], 1) # clockwise 90
        elif face == 'left':
            self._state['up'] = np.rot90(self._state['up'], 1)
            self._state['down'] = np.rot90(self._state['down'], 3)
        elif face == 'up':
            self._state['right'] = np.rot90(self._state['right'], 1)
            self._state['left'] = np.rot90(self._state['left'], 3)
            self._state['back'] = np.rot90(self._state['back'], 2)
        elif face == 'down':
            self._state['right'] = np.rot90(self._state['right'], 3)
            self._state['left'] = np.rot90(self._state['left'], 1)
            self._state['back'] = np.rot90(self._state['back'], 2)

    def _deselect(self, face):
        """Returns faces to original orientation
        """
        if face == 'front':
            pass
        elif face == 'back':
            self._state['up'] = np.rot90(self._state['up'], 2)
            self._state['down'] = np.rot90(self._state['down'], 2)
        elif face == 'right':
            self._state['up'] = np.rot90(self._state['up'], 1)
            self._state['down'] = np.rot90(self._state['down'], 3)
        elif face == 'left':
            self._state['up'] = np.rot90(self._state['up'], 3)
            self._state['down'] = np.rot90(self._state['down'], 1)
        elif face == 'up':
            self._state['right'] = np.rot90(self._state['right'], 3)
            self._state['left'] = np.rot90(self._state['left'], 1)
            self._state['back'] = np.rot90(self._state['back'], 2)
        elif face == 'down':
            self._state['right'] = np.rot90(self._state['right'], 1)
            self._state['left'] = np.rot90(self._state['left'], 3)
            self._state['back'] = np.rot90(self._state['back'], 2)

    def _shift_sides(self, face, dir_):
        """Moves the pieces of the adjacent sides when rotating
        """
        if face == 'front':
            faces = ['up','right','down','left']
        elif face == 'back':
            faces = ['up','left','down','right']
        elif face == 'right':
            faces = ['up','back','down','front']
        elif face == 'left':
            faces = ['up','front','down','back']
        elif face == 'up':
            faces = ['back','right','front','left']
        else:
            faces = ['front','right','back','left']

        bot_row = copy(self._state[faces[0]][2, :])
        left_col = copy(self._state[faces[1]][:, 0])
        top_row = copy(self._state[faces[2]][0, :])
        right_col = copy(self._state[faces[3]][:, 2])

        if dir_ == 'r':
            self._state[faces[0]][2, :] = right_col
            self._state[faces[1]][:, 0] = bot_row
            self._state[faces[2]][0, :] = left_col
            self._state[faces[3]][:, 2] = top_row
        else:
            self._state[faces[0]][2, :] = left_col
            self._state[faces[1]][:, 0] = top_row
            self._state[faces[2]][0, :] = right_col
            self._state[faces[3]][:, 2] = bot_row

if __name__ == "__main__":
    c = Cube()
    print c
    print c.is_solved()
    c.rotate('back', 'l').rotate('back', 'r')
    print c
    print c.is_solved()
    # c.rotate('front', 'l')
    # print c
    c.shuffle()
    print c
    print c.is_solved()
