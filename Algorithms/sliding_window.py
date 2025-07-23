# The Sliding Window Technique is a powerful method used to solve problems involving arrays or strings, 
# particularly when you need to analyze a subrange (or "window") of elements that moves across the data structure.

# 🔍 Concept
# Instead of recomputing values for each window from scratch, you reuse results from the previous window by 
# adding the new element and removing the old one as the window slides forward.

# 💡 When to Use Sliding Window
# Problems involving subarrays or substrings

# Need to find:

# Maximum/minimum sum in a window

# Longest/shortest subarray with a condition

# Fixed-size or variable-size windows

# 📐 Types of Sliding Windows
# Fixed-size window – size k is given
# Variable-size window – size changes based on some condition (e.g. sum < target)

# ✅ Fixed-Size Window Example
# Problem: Find the maximum sum of any subarray of size k.
def max_sum_subarray(arr, k):
    window_sum = sum(arr[:k])
    max_sum = window_sum

    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]  # slide window right
        max_sum = max(max_sum, window_sum)

    return max_sum

# Example
print(max_sum_subarray([2, 1, 5, 1, 3, 2], 3))  # Output: 9


# ✅ Variable-Size Window Example
# Problem: Find the smallest subarray with sum ≥ target

def min_subarray_len(target, nums):
    left = 0
    total = 0
    min_len = float('inf')

    for right in range(len(nums)):
        total += nums[right]
        while total >= target:
            min_len = min(min_len, right - left + 1)
            total -= nums[left]
            left += 1

    return min_len if min_len != float('inf') else 0

# Example
print(min_subarray_len(7, [2, 3, 1, 2, 4, 3]))  # Output: 2

# 🧠 Key Benefits
# Reduces time complexity from O(n*k) to O(n)

# Efficient for problems with contiguous elements

# 🗂️ Real-world Use Cases
# Data stream processing (e.g., moving averages)

# Substring search

# Network packet analysis

# Game development (e.g., event windows)

