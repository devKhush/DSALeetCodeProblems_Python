# https://leetcode.com/problems/plus-one/

class Solution(object):

    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1

        for i in range(len(digits) - 1, -1, -1):
            sum_in_str = str(carry + digits[i])
            if len(sum_in_str) == 2:
                carry = int(sum_in_str[0])
                digits[i] = int(sum_in_str[1])
            elif len(sum_in_str) == 1:
                digits[i] = int(sum_in_str[0])
                carry = 0

        if carry != 0:
            new_digits = [carry]
            for i in digits:
                new_digits.append(i)
            return new_digits

        return digits


num = [9]
obj = Solution()
print(obj.plusOne(num))
