import abc
import math
from cube import Cube

class SolverError(Exception):
    pass

class SolverBase(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def load(self, cube):
        """Loads the cube"""
        return 

    @abc.abstractmethod
    def solve(self):
        """Returns a list of moves that solves the cube
        """
        return 

class Node(object):

    def __init__(self, state):
        self.state = state
        self.children = {}
        self.parent = None
        self.value = 0.
        self.visit_count = 0

def UCB(value, bias, parent_n, n):
    """Upper Confidence Bounds formula"""
    return value + bias * math.sqrt(math.log(parent_n) / n)

class MCTSSolver(SolverBase):

    def __init__(self, bias=1.0, depth_limit=30):
        self.root = None
        self.bias = bias
        self.cube = None
        self.depth_limit = depth_limit
        
    def load(self, cube):
        self.cube = cube
        self.root = Node(cube.state)

    def save_tree(self):
        """Saves the current tree into a JSON file"""
        raise NotImplementedError('TODO')

    def load_tree(self, filename):
        """Loads a previously saved tree from a JSON file"""
        raise NotImplementedError('TODO')

    def solve(self):
        if not cube:
            raise SolverError('Cube not loaded yet')

        node = self.select()
        result = self.simulate(node)
        self.backpropagate(result, node)

    def select(self):
        """Selects and returns a leaf node to simulate"""
        raise NotImplementedError('TODO')

    def simulate(self, node):
        """Given a node, simulate until cube is solved or depth limit is reached
        """
        raise NotImplementedError('TODO')

    def backpropagate(self, result, node):
        """Given the result of the simulation, update nodes
        from `node` to root
        """
        raise NotImplementedError('TODO')
            





