"""

"""
import random
import time


def binary_search(input, target, low, high):

    middle = int((low + high) / 2)

    if low > high:
        return -1

    if input[middle] == target:
        return middle
    elif input[middle] > target:
        return binary_search(input, target, low, middle-1)
    else:
        return binary_search(input, target, middle+1, high)


def count_occurrences(input, target, low, high):
    upper = upper_boundary(input, target, low, high)
    lower = lower_boundary(input, target, low, high)
    print(lower, upper)
    return upper - lower


def upper_boundary(input, target, low, high):
    middle = int((low + high) / 2)

    if low > high:
        return low

    if input[middle] > target:
        return upper_boundary(input, target, low, middle - 1)
    else:
        return upper_boundary(input, target, middle + 1, high)


def lower_boundary(input, target, low, high):
    middle = int((low + high) / 2)

    if low > high:
        return low

    if input[middle] < target:
        return lower_boundary(input, target, middle + 1, high)
    else:
        return lower_boundary(input, target, low, middle - 1)


def one_sided():
    """ Implement a one sided binary search. """
    pass


if __name__ == "__main__":

    binary_search_times = []
    built_in_search_times = []

    iterations = 10

    for i in range(iterations):
        input = [random.randint(0, 10000) for _ in range(10000000)]
        input.sort()
        target = random.choice(input)

        t0 = time.perf_counter()
        binary_search(input, target, 0, len(input))
        binary_search_times.append(time.perf_counter() - t0)

        t0 = time.perf_counter()
        input.index(target)
        built_in_search_times.append(time.perf_counter() - t0)

    print(sum(built_in_search_times) / len(built_in_search_times))
    print(sum(binary_search_times) / len(binary_search_times))
