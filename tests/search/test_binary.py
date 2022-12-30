"""

"""

import unittest
import random


class TestBinarySearch(unittest.TestCase):

    def test_search(self):
        from algorithms.search.binary import binary_search
        input = [random.randint(0, 100) for _ in range(10)]
        input.sort()
        target = random.choice(input)
        target_index = binary_search(input, target, 0, len(input))
        self.assertEqual(target, input[target_index])

    def test_count_occurrences(self):
        from algorithms.search.binary import count_occurrences
        input = [0, 0, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        target = 1
        occurrences = count_occurrences(input, target, 0, len(input))
        self.assertEqual(3, occurrences)
