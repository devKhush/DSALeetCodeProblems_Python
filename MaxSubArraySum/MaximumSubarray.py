from typing import List


# https://leetcode.com/problems/maximum-subarray/

class Solution:

    def maxSubArray1(self, nums: List[int]) -> int:
        # below one is brute force, calculates sum of each sub array
        max_sum = nums[0]
        for i in range(len(nums)):
            all_elements_sum = 0
            for j in range(i, len(nums)):
                all_elements_sum += nums[j]
                if all_elements_sum > max_sum:
                    max_sum = all_elements_sum

        return max_sum

    def maxSubArray2(self, nums: List[int]) -> int:
        # Kadane's Algorithm
        # Time complexity -> O(n), Space complexity -> O(1)
        max_sum = nums[0]
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            max_sum = sum if sum > max_sum else max_sum
            if sum < 0:
                sum = 0

        return max_sum


arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
obj = Solution()
print(obj.maxSubArray2(arr))
