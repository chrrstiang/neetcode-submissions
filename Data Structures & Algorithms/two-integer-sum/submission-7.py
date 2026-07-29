class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffs = {}

        for i, num in enumerate(nums):
            diffs[num] = i
        
        for i, num in enumerate(nums):
            diff = target - num
            if diff in diffs and not i == diffs[diff]:
                return [i, diffs[diff]]