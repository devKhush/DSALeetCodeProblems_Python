from typing import List


class Solution:

    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        mid = 0
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1

        return mid+1 if target > nums[mid] else mid

    def searchInsert(self, nums: List[int], target: int) -> int:
        index = self.search(nums, target)
        return index




list_num = [1, 3, 5, 6]
print(Solution().search(list_num, 4))
