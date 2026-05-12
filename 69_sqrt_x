class Solution:
    def mySqrt(self, x: int) -> int:
        sqrt = 1
        while sqrt*sqrt < x:
            sqrt += 1

        if sqrt*sqrt > x:
            sqrt -= 1

        return sqrt



if __name__ == '__main__':
    solution = Solution()
    print(solution.mySqrt(4))
    print(solution.mySqrt(8))