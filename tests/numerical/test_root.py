"""

"""

import unittest


class TestRoot(unittest.TestCase):

    def test_root(self):
        from algorithms.numerical.root import square_root
        tests = [25, 100, -25, -100, 0, 10000]
        answers = [5, 10, -1, -1, -1, 100]
        for value, answer in zip(tests, answers):
            with self.subTest(value=value):
                root = square_root(value, 1, value, 100)
                self.assertAlmostEqual(root, answer)

