class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffs = {}
        for i in range(len(nums)):
            diffs[nums[i]] = i
        
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in diffs and i != diffs[diff]:
                print(f'diff is {diff} and i is {i}')
                return [i, diffs[diff]]