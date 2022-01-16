from typing import List


class Solution:

    def factorial(self, n: int) -> int:
        fact = 1
        for i in range(1, n+1):
            fact *= i
        return fact

    def combination(self, n: int, r: int) -> int:
        return self.factorial(n) // (self.factorial(n-r) * self.factorial(r))

    def generate(self, numRows: int) -> List[List[int]]:
        pascal_triangles = list()
        for i in range(numRows):
            inner_list = []
            for j in range(i+1):
                inner_list.append(self.combination(i,j))
            pascal_triangles.append(inner_list)
        return pascal_triangles


print(Solution().generate(5))

