# The optimal solution for Leetcode 238: Product of Array Except 
# Self must run in O(n) time and without using division, and with O(1) extra space (excluding the output array).

# ✅ Optimal Solution (Python) – O(n) time, O(1) space (excluding output)
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        # Left pass: res[i] contains the product of all elements to the left of i
        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]

        # Right pass: multiply res[i] by the product of all elements to the right of i
        suffix = 1
        for i in reversed(range(n)):
            res[i] *= suffix
            suffix *= nums[i]

        return res

# 🔍 Explanation
# First pass (left to right):

# At each index i, store the product of all elements to the left of i.

# Second pass (right to left):

# Multiply the stored value at res[i] with the product of all elements to the right of i.

# 🔧 Example
# Input:

# python
# Copy
# Edit
# nums = [1, 2, 3, 4]
# Step-by-step:

# After first pass: res = [1, 1, 2, 6]
# (prefixes: 1, 1×1=1, 1×2=2, 2×3=6)

# After second pass: res = [24, 12, 8, 6]
# (suffixes: 4×3×2=24, 4×3=12, 4×1=8, 1×1=6)

# ✅ Constraints Handled:
# No division

# O(n) time

# O(1) extra space (output array not counted)