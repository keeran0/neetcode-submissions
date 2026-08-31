class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}

        for i, num in enumerate(nums):
            num2 = target - num
            if num2 in indices:
                return [indices[num2], i]
            else:
                indices[num] = i

        return null
        