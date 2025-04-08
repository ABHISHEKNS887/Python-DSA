# Big 0:
# Big O notation is a way to describe the performance or complexity of an algorithm in terms of time (execution time) or 
# space (memory usage) as the input size grows. It provides a high-level understanding of the worst-case scenario, helping to 
# evaluate how efficiently an algorithm scales.

# Key Big O Notations
# O(1) - Constant Time

# The runtime does not depend on the size of the input.
# Example: Accessing an element in an array by its index.
# Example Code:

def get_first_element(arr):
    return arr[0]

# O(log n) - Logarithmic Time
# The runtime grows logarithmically as the input size increases.
# Often seen in divide-and-conquer algorithms (e.g., binary search).
# Example Code:

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# O(n) - Linear Time

# The runtime grows proportionally to the input size.
# Example: Iterating through all elements in a list.
# Example Code:

def find_element(arr, target):
    for element in arr:
        if element == target:
            return True
    return False

# -------------------------------------------------------------------------------------------------------------------------------

# Drop constant:
# consider we have 2 seperate for loop in a function. so it will be n+n=2n. so this will be o(2n).
# So here we will drop the constant. So if it is 2n or 10n. we will consider it as o(n).

# -------------------------------------------------------------------------------------------------------------------------------
# o(n^2):
# If there a for loop insider the for loop then it is considered as o(n^2).

# if we have both n^2 + n in a function. we will drop n. So we will drop non dominance.
# so it will be o(n^2)

# -------------------------------------------------------------------------------------------------------------------------

# different terms of inputs: consider we have 2 arguments in a function. i.e a and b. and consider we will have 2 for loops. 
# so bigo will be a+b or axb.
# -------------------------------------------------------------------------------------------------------------------------

# consider if we want to remove or add a value at the end of list. so it will be o(1). BCZ no reindexing happens. 
# if we want to remove or add the value at the starting or in the middle of this list. that will be 0(n). BCZ here reindexing happens.