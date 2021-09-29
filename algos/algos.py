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
    j = 1
    while not (i > high or j > high):
        # 19 78 49 69 26
        # 19 78 49 | 69 26
        # 19 78 | 49
        # 19 | 78
        # 19 78 | 49 i++, *(i j) i++ j++, i > mid j > high
        # 19 49 78 | 69 26
        # 69 | 26
        # 26 69
        # 19 48 78 | 26 69 i++, *(i j) i++ j++, *(i j) *(i j-1) i++ j++, i > mid j > high
        # 19 26 48 69 78
        # 
        # 40 32 45 42 67
        # 40 32 45 | 42 67
        # 40 32 | 45
        # 40 | 32
        # 32 40 | 45 i++, i++, i > mid
        # 32 40 45 | 42 67
        # 42 | 67
        # 32 40 45 | 42 67 i++, i++, *(i j) i++ j++, i++, i++, i > high
        # 32 40 42 45 67
        low_value = array[low + i]
        high_value = array[mid + j]

        if low_value > high_value:
            swap(low + i, mid + j, array)
            if j > 0:
                if array[low + i] > array[mid + j - 1]:
                    swap(low + i, mid + j - 1, array)
            j += 1
        elif j > 0:
            swap(low + i, mid + j - 1, array)
        i += 1
        # elif j == 0 and i < mid + 1:
        #     if array[low + i] > array[mid + j + 1]:
        #         swap(low + i, mid + j + 1, array)
        #         j += 1
        # elif j > 0 and i < mid + 1:
        #     if array[low + i] > array[mid + j + 1]:
        #         swap(low + i, mid + j + 1, array)
        #         j += 1
        #     else:
        #         swap(low + i, mid + j, array)
        # elif i >= mid + 1:
        #     if array[mid + j] > array[mid + j + 1]:
        #         swap(mid + j, mid + j + 1, array)
        #         j += 1

def merge_helper(low: int, high: int, array: List[T]):
    mid = (high + low) // 2
    if low == mid:
        merge(low, mid, high, array)
    else:
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
