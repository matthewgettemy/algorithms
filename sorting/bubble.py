"""
Bubble sort iterates over the array of input, and compares
consecutive numbers. If the first number is larger it swaps
the numbers, otherwise leave them in place.

Bubble sort is not good to use in practice because it has worst
and average case time complexity of O(n^2).

High numbers towards the beginning of the array are called rabbits
because they are quickly moved to the end of the array, low numbers
at the end are slowly moved to the front, and can only be moved one
place each time the array is iterated over.
"""

import numpy as np
import random
import time
import matplotlib.pyplot as plt


def bubblesort(input):
    flipped = True
    while flipped:
        flipped = False
        for i, value in enumerate(input):
            if (i + 1) == len(input):
                continue
            if value > input[i+1]:
                input[i] = input[i+1]
                input[i+1] = value
                flipped = True



if __name__ == "__main__":

    ns = [100 * n for n in range(100)]
    runtimes = []
    for n in ns:
        input = [random.randint(1, 10000) for _ in range(n)]
        t0 = time.perf_counter()
        bubblesort(input)
        runtime = time.perf_counter() - t0
        runtimes.append(runtime)
        print(n, runtime)

    """
    The act of transforming a polynomial function into an exponential one
    has the effect of increasing large values much more than it does small
    values, and thus it has the effect of increasing the distance to the
    fitted curve for large values more than it does for small values. This
    can be mitigated by adding a ‘weight’ proportional to y: tell polyfit()
    to lend more importance to data points with a large y-value:
    """
    poly = np.polyfit(x=ns, y=np.log(runtimes), deg=1, w=np.sqrt(runtimes))
    a = np.exp(poly[1])
    b = poly[0]
    x_fitted = np.linspace(np.min(ns), np.max(ns), 100)
    y_fitted = a * np.exp(b * x_fitted)

    ax = plt.axes()
    ax.plot(ns, runtimes, "o", color="darkblue", label="runtimes", mfc="none")
    ax.plot(x_fitted, y_fitted, "k", linewidth=1, label='Fitted Function:\n $t = %0.6f e^{%0.6f n}$' % (a, b))
    ax.set_xlabel("n")
    ax.set_ylabel("time [s]")
    ax.grid()
    ax.legend()
    plt.show()
