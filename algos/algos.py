from typing import TypeVar, List

T = TypeVar('T', int, float)

def binary_search(value: T, array: List[T]) -> int:
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = (high + low) // 2
        if array[mid] == value:
            return mid
        elif array[mid] < value:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def fibonacci(n: int) -> int:
    """
    This implementation is inneficient!
    """
    if n < 2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

def fibonacci_plus_plus(n: int) -> int:
    next = 1
    middle = 1
    previous = 0
    for _ in range(n):
        previous_stored = previous
        middle_stored = middle

        previous = middle
        middle += previous_stored
        next += middle_stored
    return middle

def swap(i: int, j: int, array: List[T]):
    stored = array[i]
    array[i] = array[j]
    array[j] = stored

def insertion_sort(array: List[T]):
    for i in range(1, len(array)):
        value = array[i]
        value_index = i
        while array[value_index - 1] > value and value_index - 1 >= 0:
            value_index -= 1
        while value_index < i:
            swap(i, value_index, array)
            value_index += 1

def merge(low: int, mid: int, high: int, array: List[T]):
    i = 0
    j = 0
    while low + i < mid + 1 and mid + i + 1 < high:
        if low + i >= mid + 1:
            pass
        elif array[low + i] > array[mid + j + 1]:
            swap(low + i, mid + i + 1, array)
            i += 1
            j += 1
        elif array[low + i] <= array[mid + j + 1]:
            i += 1
            # 25 7 84 60 72
            # 25 7 84 | 60 72
            # 25 7 | 84
            # 25 | 7
            # 7 25 | 84
            # 7 25 84
            # 
            # 60 | 72
            # 60 72
            #
            # 7 25 84 | 60 72 i++
            # 7 25 84 | 60 72 i++
            # 7 25 60 | 84 72 i++ j++
            # 7 25 60 | 72 84 j++
            #
            # 1 4 7 2 3 9
            # 1 4 7 | 2 3 9
            # 1 4 | 7
            # 1 | 4
            #
            # 2 3 | 9
            # 2 | 3
            #
            # 1 4 7 | 2 3 9
            # 1 2 7 | 4 3 9
            # 1 2 3 | 4 7 9

def merge_helper(low: int, high: int, array: List[T]):
    mid = (high + low) // 2
    if low == mid:
        merge(low, mid, high, array)
    merge_helper(low, mid, array)
    merge_helper(mid+1, high, array)
    merge(low, mid, high, array)

def merge_sort(array: List[T]):
    low = 0
    high = len(array) - 1
    mid = (low + high) // 2
    merge_helper(low, mid, array)
    merge_helper(mid+1, high, array)
    merge(low, mid, high, array)

def gcd(a: int, b: int) -> int:
    # check if a is inded larger or equal to b
    if a < b:
        swap = a
        a = b
        b = swap
    if b == 0:
        return a
    elif a % b == 0:
        return b
    return gcd(b, a % b)
