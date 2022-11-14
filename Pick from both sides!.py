from functools import reduce
from typing import List


def solve(array: List[int], number_of_elements: int) -> int:
    max_sum = reduce(lambda a, b: a+b, array[: number_of_elements])
    compare_sum = max_sum
    for i, j in zip((range(number_of_elements - 1, -1, -1)),
                    (range(-1, -(number_of_elements + 1), -1))):
        try:
            compare_sum -= array[i]
            compare_sum += array[j]
            max_sum = max(compare_sum, max_sum)
        except IndexError as err:
            raise Exception("number_of_elements must be less then the length "
                            "of array")
    return max_sum


if __name__ == "__main__":
    print(solve([-533, -666, -500, 169, 724, 478, 358, -38, -536, 705, -855,
                 281, -173, 961, -509, -5, 942, -173, 436, -609, -396, 902,
                 -847, -708, -618, 421, -284, 718, 895, 447, 726, -229, 538,
                 869, 912, 667, -701, 35, 894, -297, 811, 322, -667, 673,
                 -336, 141, 711, -747, -132, 547, 644, -338, -243, -963,
                 -141, -277, 741, 529, -222, -684, 35], 48))
    print(solve([5, -2, 3, 1, 2], 3))
    print(solve([-5, 2, 3, 1, -2], 3))
    print(solve([5, -2, -3, 1, 2], 3))
    print(solve([5, -2, 2, -1, 2], 3))
    print(solve([1, 2], 3))
