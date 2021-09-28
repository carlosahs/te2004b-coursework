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
        while array[value_index - 1] > value:
            value_index -= 1
        while value_index < i:
            swap(i, value_index, array)
            value_index += 1

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
