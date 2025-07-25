# Given an integer array nums, find the subarray with the largest sum, and return its sum.

# Example 1:

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.
# Example 2:

# Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum 1.
# Example 3:

# Input: nums = [5,4,-1,7,8]
# Output: 23
# Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

class Solution:
    def maxSubArray(self, nums) -> int:
        _max = nums[0]
        _sum = 0
        for i in nums:
            if _sum < 0:
                _sum = 0
                
            _sum += i

            if _sum > _max:
                _max = _sum

        return _max
# The above code implements Kadane's algorithm to find the maximum subarray sum.
# It initializes the maximum sum to the first element and iterates through the array,
# resetting the current sum to zero if it becomes negative. It updates the maximum sum whenever a
# larger sum is found. The time complexity is O(n) and the space complexity is O(1), as it uses only a few variables for tracking the sums. 
# 🧪 Test Cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    nums1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print("Test Case 1 Output:", solution.maxSubArray(nums1))  # Expected: 6

    # Test case 2
    nums2 = [1]
    print("Test Case 2 Output:", solution.maxSubArray(nums2))  # Expected: 1

    # Test case 3
    nums3 = [5, 4, -1, 7, 8]
    print("Test Case 3 Output:", solution.maxSubArray(nums3))  # Expected: 23


