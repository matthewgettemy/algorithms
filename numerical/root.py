"""

"""

import math


def square_root(number, lower, root, rounds):

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
    number = 151251
    rounds = 100
    root = square_root(number, 1, number, rounds)
    print(root)
