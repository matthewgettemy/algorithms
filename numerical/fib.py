"""

"""

import time


def fibonacci(nth):

    if nth <= 1:
        return nth

    return fibonacci(nth - 1) + fibonacci(nth - 2)



if __name__ == "__main__":
    """
    index  = 0, 1, 2, 3, 4, 5, 6,  7,  8
    number = 1, 1, 2, 3, 5, 8, 13, 21, 34
    """

    runtimes = []
    iterations = 40

    for i in range(1, iterations):
        print(i)
        t0 = time.perf_counter()
        result = fibonacci(i)
        execution_time = time.perf_counter() - t0
        runtimes.append(execution_time)

    for i, runtime in enumerate(runtimes):
        print(i, runtime)



