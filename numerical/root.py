"""

"""

import math
import random
import time


def square_root(number, lower, root, rounds):
    """
    Less efficient than the built in math.sqrt. the built in algo probably uses
    interpolation to find a test point closer to the actual root instead of
    always using the midpoint.
    """

    rounds -= 1

    if number < 1:
        return -1

    if rounds <= 0:
        return root

    m = (lower + root) / 2
    m_squared = m * m

    if number >= m_squared:
        return square_root(number, m, root, rounds)
    else:
        return square_root(number, lower, m, rounds)



if __name__ == "__main__":
    bisection_square_root_times = []
    builtin_square_root_times = []

    ints = [random.randint(1, 1000000) for _ in range(10000)]
    for i in ints:
        t0 = time.perf_counter()
        result = math.sqrt(i)
        builtin_square_root_times.append(time.perf_counter() - t0)

        t0 = time.perf_counter()
        result = square_root(i, 1, i, 100)
        bisection_square_root_times.append(time.perf_counter() - t0)

    print(sum(builtin_square_root_times) / len(builtin_square_root_times))
    print(sum(bisection_square_root_times) / len(bisection_square_root_times))
