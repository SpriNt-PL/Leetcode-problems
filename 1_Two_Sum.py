class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, left_side in enumerate(nums):
            for j, right_side in enumerate(nums):
                if left_side + right_side == target:
                    result = [i, j]
                    print(result)
                    return result 


if __name__ == '__main__':
    solution = Solution()

    nums = [2,7,11,15]
    target = 9
    assert solution.twoSum(nums, target) == [0,1]

    nums = [3,2,4]
    target = 6
    assert solution.twoSum(nums, target) == [1,2]