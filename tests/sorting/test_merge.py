"""

"""

import unittest
import random


class TestMerge(unittest.TestCase):

    def test_mergesort(self):
        from algorithms.sorting.merge import mergesort
        random_input = [random.randint(1, 1000000) for _ in range(1000)]
        result = mergesort(random_input)
        self.assertEqual(random_input.sort(), result)
