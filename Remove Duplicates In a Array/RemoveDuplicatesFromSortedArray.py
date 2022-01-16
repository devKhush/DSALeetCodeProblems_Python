from typing import List


class Solution:

    # assuming nums is sorted, if not do it
    def removeDuplicates(self, nums: List[int]) -> int:

        # length is actual non-repeated array's length

        length: int = 1
        if len(nums) < 1:
            return 0
        for i in range(len(nums)):
            if nums[length-1] != nums[i]:
                nums[length] = nums[i]
                length += 1

        return length


numbers = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print(Solution().removeDuplicates(numbers))
print(numbers)





