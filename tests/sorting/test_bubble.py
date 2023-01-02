"""

"""



import unittest
import copy


class TestBubble(unittest.TestCase):

    def test_bubblesort(self):
        from algorithms.sorting.bubble import bubblesort
        input = [-1, 0, 1, 5, 8, -9, 4]
        bubble_input = copy.copy(input)
        bubblesort(bubble_input)
        input.sort()
        self.assertEqual(input, bubble_input)
