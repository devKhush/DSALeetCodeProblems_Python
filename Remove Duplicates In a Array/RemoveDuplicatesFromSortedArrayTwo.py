from typing import List


class Solution:

    # assuming nums is sorted, if not do it
    def removeDuplicates(self, arr: List[int]) -> int:

        # 'length' is actual length according to problem
        length = 1
        count_of_element = 1

        for i in range(1, len(arr)):
            if arr[i] == arr[length - 1] and count_of_element <= 1:
                arr[length] = arr[i]
                count_of_element += 1
                length += 1

            elif arr[i] != arr[length - 1]:
                arr[length] = arr[i]
                count_of_element = 1
                length += 1

        return length

    # another faster approach
    def remove_duplicate_faster(self, arr: List[int]) -> int:

        if len(arr) <= 2:
            return len(arr)

        length = 2
        for i in range(2, len(arr)):
            if arr[length - 2] != arr[i]:
                arr[length] = arr[i]
                length += 1
        return length


nums = [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 2, 6, 6, 6, 6, 7, 7, 7, 7, 7, 8, 9, 11, 11, 11, 11]
obj = Solution()
print(obj.remove_duplicate_faster(nums))
print(nums)
print(0 in nums)


