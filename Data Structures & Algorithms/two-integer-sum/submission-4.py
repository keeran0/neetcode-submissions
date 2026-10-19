class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        vals = {}

        for i, num in enumerate(nums):
            target_v = target - num

            if target_v in vals:
                return [vals[target_v], i]
            
            vals[num] = i

        return [0]

        