"""
Rubiks cube class
"""

import numpy as np

class Cube(object):
    def __init__(self):
        self._state = {'front': np.chararray((3,3)),
                      'back': np.chararray((3,3)),
                      'right': np.chararray((3,3)),
                      'left': np.chararray((3,3)),
                      'up': np.chararray((3,3)),
                      'down': np.chararray((3,3))}

        colors = ['b','g','r','o','y','w']
        for face, color in zip(self._state.keys(), colors):
            self._state[face][:] = color

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
        pass

    def rotate(self, dir):
        pass
