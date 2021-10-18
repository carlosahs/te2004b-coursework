from collections import defaultdict
from typing import Dict
from typing import List

# nCk = n! / (k! * (n - k)!)
# []
# [1], [2], [3], [4], [5]
# [1,2], [1,3], [1,4], [1,5], [2,3], [2,4], [2,5], [3,4], [3,5], [4,5]
# [1,2,3], [1,2,4], [1,2,5], [1,3,4], [1,3,5], [1,4,5], [2,3,4], [2,3,5], 
#   [2,4,5], [3,4,5]
# [1,2,3,4], [1,2,3,5], [1,2,3,5], [1,3,4,5], [2,3,4,5]
# [1,2,3,4,5]

def factorial(nth: int) -> int:
    if nth <= 1:
        return 1

    n = 2
    for i in range(3, nth + 1):
        n *= i

    return n

def combinations(n: int, k: int) -> int:
    return factorial(n) // (factorial(k) * factorial(n - k))

def get_subsets(elements: List[int]) -> defaultdict[int, defaultdict[int, List[int]]]:
    coefficients = []
    subsets = defaultdict(lambda: defaultdict(list))
    len_elements = len(elements)

    for i in range(0, len_elements + 1):
        coefficients.append(combinations(len_elements, i))

    for idx in range(0, len_elements):
        for i in range(1, len_elements):
            if i == 1:
                subsets[idx][i].append([elements[idx]])
            else:
                for subset in subsets[idx][i-1]:
                    j = idx + i - 1
                    while j != len_elements:
                        subsets[idx][i].append(subset + [elements[j]])
                        j += 1

    return subsets

# [1,2,3,4,5]
# [1]
# [1,2], [1,3], [1,4], [1,5]
# [1,2,3], [1,3,4], [1,4,5]
# [1,2,3,4], [1,3,4,5]

# [2]
# [2,3], [2,4], [2,5]
# [2,3,4], [2,4,5]
# [2,3,4,5]

# [1,2,3]
# [1]
# [1,2], [1,3]

# [2]
# [2,3]

# [3]

# [1,2,3,4]
# [1]
# [1,2], [1,3], [1,4]
# [1,2,3], [1,3,4, [1,4,5]
