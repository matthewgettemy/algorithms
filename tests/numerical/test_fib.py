"""

"""

import unittest



class TestFibonacci(unittest.TestCase):

    def test_fibonacci(self):
        from algorithms.numerical.fib import fibonacci
        nth = 10
        answer = 55
        result = fibonacci(nth)
        self.assertEqual(result, answer)

    def test_nonrecursive_fibonacci(self):
        from algorithms.numerical.fib import nonrecursive_fibonacci
        nth = 10
        answer = 55
        result = nonrecursive_fibonacci(10)
        self.assertEqual(result, answer)