"""

"""

import time
import matplotlib.pyplot as plt

def fibonacci(nth):

    if nth <= 1:
        return nth

    return fibonacci(nth - 1) + fibonacci(nth - 2)


def nonrecursive_fibonacci(nth):

    if nth == 1:
        return 1

    two_previous = 0
    previous = 1
    total = 0
    i = 1
    while i < nth:
        total = previous + two_previous
        two_previous = previous
        previous = total
        i += 1
    return total


if __name__ == "__main__":
    """
    index  = 0, 1, 2, 3, 4, 5, 6,  7,  8
    number = 1, 1, 2, 3, 5, 8, 13, 21, 34
    """

    recursive_runtimes = []
    nonrecursive_runtimes = []
    iterations = 40

    for i in range(1, iterations):
        print(f"Calculating the {i}th fibonacci number...")
        t0 = time.perf_counter()
        result = fibonacci(i)
        execution_time = time.perf_counter() - t0
        recursive_runtimes.append(execution_time)

        t0 = time.perf_counter()
        result = nonrecursive_fibonacci(i)
        execution_time = time.perf_counter() - t0
        nonrecursive_runtimes.append(execution_time)

    for i, runtime in enumerate(recursive_runtimes):
        print(i, runtime, nonrecursive_runtimes[i])

    ax = plt.axes()
    ax.plot(range(iterations-1), recursive_runtimes, "o", color="darkblue", label="recursive runtimes", mfc="none")
    ax.plot(range(iterations-1), nonrecursive_runtimes, "o", color="darkred", label="non-recursive runtimes", mfc="none")

    ax.set_xlabel("n")
    ax.set_ylabel("time [s], log")
    ax.grid()
    ax.legend()
    plt.yscale("log")
    plt.title("Runtimes Calculating the nth Fibonacci Number")
    plt.show()
