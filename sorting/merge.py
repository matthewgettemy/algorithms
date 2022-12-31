"""

"""

import copy
import time
import random


def mergesort(input: []):
    length = len(input)
    if length > 1:
        middle = int(length / 2)
        first_half = input[:middle]
        second_half = input[middle:]

        mergesort(first_half)
        mergesort(second_half)

        i = j = k = 0
        while i < len(first_half) and j < len(second_half):
            if first_half[i] < second_half[j]:
                input[k] = first_half[i]
                i += 1
            else:
                input[k] = second_half[j]
                j += 1
            k += 1

        while i < len(first_half):
            input[k] = first_half[i]
            i += 1
            k += 1

        while j < len(second_half):
            input[k] = second_half[j]
            j += 1
            k += 1


def merge(input1: [], input2: []):
    output = []
    while input1 and input2:
        if input1[0] < input2[0]:
            output.append(input1.pop(0))
        elif input2[0] < input1[0]:
            output.append(input2.pop(0))
        else:
            output.append(input1.pop(0))
    if input1:
        output.extend(input1)
    elif input2:
        output.extend(input2)
    return output


if __name__ == "__main__":
    input1 = [-1, 0, 2, 3, 4, 5]
    input2 = [-2, 3, 4, 5, 6]
    result = merge(input1, input2)
    print(result)

    random_lists = [
        [random.randint(-999, 999) for _ in range(5000)]
        for _ in range(100)
    ]

    sort_runtimes = []
    mergesort_runtimes = []

    for random_list in random_lists:
        c = copy.copy(random_list)
        t0 = time.perf_counter()
        sorted(c)
        sort_runtimes.append(time.perf_counter() - t0)

        c = copy.copy(random_list)
        t0 = time.perf_counter()
        mergesort(c)
        mergesort_runtimes.append(time.perf_counter() - t0)

    print(f"built in sorting: {sum(sort_runtimes) / len(sort_runtimes)}")
    print(f"custom mergesort: {sum(mergesort_runtimes) / len(mergesort_runtimes)}")
