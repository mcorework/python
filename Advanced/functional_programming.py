"""
# 🛠 Functional Programming in Python — Documentation

## 📘 Overview
Functional programming (FP) is a programming paradigm that **treats computation as the evaluation of mathematical functions** 
and avoids changing state and mutable data. Python supports functional programming features, even though it is primarily imperative.

Key concepts in functional programming include:
- **Immutability**
- **Higher-order functions**
- **Recursion**
- **Pattern matching**
- **Comprehensions**
- **Lazy evaluation**
- **Performance considerations**

### 3. Links
[Functional Programming - Arjan Codes](https://www.youtube.com/watch?v=Rp9Ha0rVM1w)

"""

from random import randint
from time import perf_counter

def bubble_sort(data: list[int]) -> list[int]:
    print(f"Data before sorting: {data}")
    n = len(data)
    for i in range(n):
        swapped = False
        for j in range(i, n - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                swapped = True
        if not swapped:
            break
    return data


def quick_sort(data: list[int]) -> list[int]:
    if len(data) <= 1:
        return data

    pivot = data[-1]
    greater = [item for item in data[:-1] if item > pivot]
    lesser = [item for item in data[:-1] if item <= pivot]
    return quick_sort(lesser) + [pivot] + quick_sort(greater)


def do_operations(data: list[int]) -> None:
    # multiply each element by 2 and add 10
    for i in range(len(data)):
        data[i] = data[i] * 2 + 10

    result = quick_sort(data)

    print(f"Result after sorting: {result}")



#=============================================================================
#🧩 1.  Recurson Technique
#=============================================================================
def quick_sort(data: list[int]) -> list[int]:
    if len(data) <= 1:
        return data

    pivot = data[-1]
    greater = [item for item in data[:-1] if item > pivot]
    lesser = [item for item in data[:-1] if item <= pivot]
    return quick_sort(lesser) + [pivot] + quick_sort(greater)

def do_operations(data: list[int]) -> None:
    # multiply each element by 2 and add 10
    for i in range(len(data)):
        data[i] = data[i] * 2 + 10
    result = quick_sort(data)
    print(f"Result after sorting: {result}")

def main() -> None:
    data = [1, 5, 3, 4, 2]
    do_operations(data)

#=============================================================================
#🧩 1.  Recurson with Iterative approach
# Bubble sort is advised in case of the list is mostly sorted
#=============================================================================
def partition(data: list[int], low: int, high: int) -> int:
    pivot = data[high]
    i = low - 1
    for j in range(low, high):
        if data[j] <= pivot:
            i += 1
            data[i], data[j] = data[j], data[i]
    data[i + 1], data[high] = data[high], data[i + 1]
    return i + 1


def quick_sort_iterative(data: list[int]) -> list[int]:
    sorted_data = data.copy()  # Work with a copy to ensure immutability
    stack: list[tuple[int, int]] = [(0, len(sorted_data) - 1)]

    while stack:
        low, high = stack.pop()
        if low < high:
            p = partition(sorted_data, low, high)
            stack.append((low, p - 1))
            stack.append((p + 1, high))

    return sorted_data


#=============================================================================
#🧩 2.Structural Pattern Matching
#=============================================================================
def quick_sort(data: list[int]) -> list[int]:
    match data:
        case []:
            return data
        case [_]:
            return data
        case _:
            pivot = data[-1]
            greater = [item for item in data[:-1] if item > pivot]
            lesser = [item for item in data[:-1] if item <= pivot]
            return quick_sort(lesser) + [pivot] + quick_sort(greater)

#=============================================================================
#🧩 3.Immutability
#=============================================================================
def quick_sort(data: list[int]) -> list[int]:
    match data:
        case []:
            return []
        case [x]:
            return [x]
        case _:
            pivot = data[-1]
            greater = [item for item in data[:-1] if item > pivot]
            lesser = [item for item in data[:-1] if item <= pivot]
            return quick_sort(lesser) + [pivot] + quick_sort(greater)


def do_operations(data: list[int]) -> None:
    transformed_data = [item * 2 + 10 for item in data] #list comprehension
    result = bubble_sort(transformed_data)

    print(f"Result after sorting - Immutability: {result}")

#=========================================================================================================
#🧩 Main Function : Result
# Note: Python does not have immutability built it, code has to be written to safeguard immutability
#=========================================================================================================

def main() -> None:
    # data = [randint(0, 10000) for _ in range(10000)]

    # start = perf_counter()
    # quick_sort(data)
    # print(f"Time taken for recursive quick sort: {perf_counter() - start:.6f} seconds")

    # start = perf_counter()
    # sorted = quick_sort_iterative(data)
    # print(f"Time taken for iterative quick sort: {perf_counter() - start:.6f} seconds")

    # start = perf_counter()
    # bubble_sort(sorted)
    # print(f"Time taken for bubble sort: {perf_counter() - start:.6f} seconds")

    data = [1, 5, 3, 4, 2]
    do_operations(data)


if __name__ == "__main__":
    main()