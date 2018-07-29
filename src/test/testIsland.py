import unittest
import numpy as np
from ..leetCode import island


class TestIsland(unittest.TestCase):
    def testIsland(self):
        test = (1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0,
                0, 0, 1, 1)
        x = np.asarray(test).reshape(5, 5)
        print('Test matrix is\n', x)
        islandNumber = island.find_independ(x)
        self.assertEqual(islandNumber, 3)


# in workspace root directory, run 
# python -m unittest src.test.testIsland or
# python -m src.test.testIsland(need main in testIsland) or
# python -m unittest discover -s src.test -v