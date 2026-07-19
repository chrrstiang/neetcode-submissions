class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        sorted_nums = sorted(nums)
        for i in range(len(nums)):
            left, right = i + 1, len(nums) - 1
            if i > 0 and sorted_nums[i] == sorted_nums[i - 1]:
                continue
            while left < right:
                result = sorted_nums[i] + sorted_nums[left] + sorted_nums[right]
                if result == 0:
                    output.append([sorted_nums[left], sorted_nums[i], sorted_nums[right]])
                    left += 1
                    right -= 1
                    while left < right and sorted_nums[left] == sorted_nums[left - 1]:
                        left += 1
                    while left < right and sorted_nums[right] == sorted_nums[right + 1]:
                        right -= 1
                elif result > 0:
                    right -= 1
                else:
                    left += 1
        return output
            