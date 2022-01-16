from typing import List


class Solution:

    def factorial(self, n: int) -> int:
        fact = 1
        for i in range(1, n+1):
            fact *= i
        return fact

    def combination(self, n: int, r: int) -> int:
        return self.factorial(n) // (self.factorial(n-r) * self.factorial(r))

    def getRow(self, rowIndex: int) -> List[int]:

        # rowIndex starts with 0
        pascal_triangle_of_a_row = []
        for j in range(rowIndex+1):
            pascal_triangle_of_a_row.append(self.combination(rowIndex, j))
        return pascal_triangle_of_a_row


print(Solution().getRow(3))

